from frozenlist2 import frozenlist

from pubtools.pulplib._impl import compat_attr as attr

from ..schema import load_schema
from .unit import Unit
from .common import PulpObject
from .attr import pulp_attrib


@attr.s(kw_only=True, frozen=True)
class Task(PulpObject):
    """Represents a Pulp task."""

    _SCHEMA = load_schema("task")

    id = pulp_attrib(type=str, pulp_field="task_id")
    """ID of this task (str)."""

    completed = pulp_attrib(default=None, type=bool)
    """True if this task has completed, successfully or otherwise.

    May be `None` if the state of this task is unknown.
    """

    succeeded = pulp_attrib(default=None, type=bool)
    """True if this task has completed successfully.

    May be `None` if the state of this task is unknown.
    """

    error_summary = pulp_attrib(default=None, type=str)
    """A summary of the reason for this task's failure (if any).

    This is a short string, generally a single line, suitable for display to users.
    The string includes the ID of the failed task.
    """

    error_details = pulp_attrib(default=None, type=str)
    """Detailed information for this task's failure (if any).

    This may be a multi-line string and may include technical information such as
    a Python backtrace generated by Pulp.

    ``error_details`` is a superset of the information available via ``error_summary``,
    so it is not necessary to display both.
    """

    tags = pulp_attrib(
        default=attr.Factory(frozenlist),
        type=list,
        converter=frozenlist,
        pulp_field="tags",
    )
    """The tags for this task.

    Typically includes info on the task's associated action and
    repo, such as:

    .. code-block:: python

        ["pulp:repository:rhel-7-server-rpms__7Server_x86_64",
         "pulp:action:publish"]
    """

    # TODO: is it a bug that this only allows a single repo ID??
    # Some tasks, like copy, involve multiple repos. We'll only include
    # the first repo ID from tags here... seems arbitrary.
    repo_id = pulp_attrib(type=str)
    """The ID of the repository associated with this task, otherwise None."""

    units = pulp_attrib(
        default=attr.Factory(frozenlist),
        type=list,
        pulp_field="result.units_successful",
        converter=frozenlist,
        pulp_py_converter=lambda raw: frozenlist(
            [Unit._from_task_data(x) for x in raw]
        ),
    )
    """Info on the units which were processed as part of this task
    (e.g. associated or unassociated).

    This is an iterable. Each element is an instance of
    :class:`~pubtools.pulplib.Unit` containing information on a processed
    unit.

    .. versionadded:: 1.5.0
    """

    units_data = pulp_attrib(
        default=attr.Factory(frozenlist),
        type=list,
        converter=frozenlist,
        pulp_field="result.units_successful",
    )
    """Info on the units which were processed as part of this task
    (e.g. associated or unassociated).

    This is a list. The list elements are the raw dicts as returned
    by Pulp. These should at least contain a 'type_id' and a 'unit_key'.

    .. deprecated:: 1.5.0
       Use :meth:`~pubtools.pulplib.Task.units` instead.
    """

    @repo_id.default
    def _repo_id_default(self):
        prefix = "pulp:repository:"
        for tag in self.tags or []:
            if tag.startswith(prefix):
                return tag[len(prefix) :]
        return None

    @succeeded.validator
    def _check_succeeded(self, _, value):
        if value and not self.completed:
            raise ValueError("Cannot have task with completed=False, succeeded=True")

    @classmethod
    def _data_to_init_args(cls, data):
        out = super(Task, cls)._data_to_init_args(data)

        state = data["state"]
        out["completed"] = state in ("finished", "error", "canceled", "skipped")
        out["succeeded"] = state in ("finished", "skipped")

        if state == "canceled":
            out["error_summary"] = "Pulp task [%s] was canceled" % data["task_id"]
            out["error_details"] = out["error_summary"]

        elif state == "error":
            out["error_summary"] = cls._error_summary(data)
            out["error_details"] = cls._error_details(data)

        return out

    @classmethod
    def _error_summary(cls, data):
        prefix = "Pulp task [%s] failed" % data["task_id"]
        error = data.get("error")
        if not error:
            return "%s: <unknown error>" % prefix
        return "%s: %s: %s" % (prefix, error["code"], error["description"])

    @classmethod
    def _error_details(cls, data):
        out = cls._error_summary(data)

        error = data.get("error")
        if not error:
            return out

        # Error looks like this:
        #
        # {
        #   'code': u'PLP0001',
        #   'data': {
        #     'message': 'a message'
        #   },
        #   'description': 'A general pulp exception occurred',
        #   'sub_errors': []
        # }
        #
        # See: https://docs.pulpproject.org/en/2.9/dev-guide/conventions/exceptions.html#error-details
        #
        # data can contain anything, or nothing.
        # It's only a convention that it often contains a message.
        #
        # sub_errors is currently ignored because I've never seen a non-empty
        # sub_errors yet.

        error_data = error.get("data") or {}
        messages = []

        # Message in a general exception
        if error_data.get("message"):
            messages.append(error_data["message"])

        # Some exceptions stash additional strings under details.errors
        if (error_data.get("details") or {}).get("errors"):
            error_messages = error_data["details"]["errors"]
            if isinstance(error_messages, list):
                messages.extend(error_messages)

        # Pulp docs refer to this as deprecated, but actually it's still
        # used and no alternative is provided.
        if data.get("traceback"):
            messages.append(data["traceback"])

        message = "\n".join(messages)
        if message:
            # message can have CRLF line endings in rare cases.
            message = message.replace("\r\n", "\n").strip()
            out = "%s:\n%s" % (out, _indent(message))

        return out


def _indent(text, level=2):
    spaces = " " * level
    return spaces + text.replace("\n", "\n" + spaces)
