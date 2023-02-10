import json
import os

import attr

from pubtools.pulplib import (
    Unit,
    ErratumUnit,
    ErratumReference,
    ErratumPackage,
    ErratumPackageCollection,
    ErratumModule,
)


def test_can_load_erratum(data_path):
    """ErratumUnit loads correctly from a complex sample Pulp response."""

    # This JSON was taken from a real Pulp search, though it was slightly trimmed
    # to reduce the size of the test data (e.g. cutting out modules for some arches,
    # cutting down the repo and package lists).
    with open(os.path.join(data_path, "sample-erratum.json"), "rt") as f:
        data = json.load(f)

    # It should parse correctly
    loaded = Unit.from_data(data)

    # It should be equal to the following...

    # Note, in order to make the test more manageable in case of failure, we verify
    # some of the more complicated nested fields first, then omit them from the
    # later comparison of the overall unit. This way the pytest output is more amenable
    # to copy-pasting values back into the test if behavior changes.
    assert loaded.references == [
        ErratumReference(
            href="https://access.redhat.com/errata/RHSA-2019:0975",
            id="RHSA-2019:0975",
            title="RHSA-2019:0975",
            type="self",
        ),
        ErratumReference(
            href="https://bugzilla.redhat.com/show_bug.cgi?id=1664908",
            id="1664908",
            title="CVE-2019-5736 runc: Execution of malicious containers allows for container escape and access to host filesystem",
            type="bugzilla",
        ),
        ErratumReference(
            href="https://bugzilla.redhat.com/show_bug.cgi?id=1695689",
            id="1695689",
            title="[stream rhel8] don't allow a container to connect to random services",
            type="bugzilla",
        ),
        ErratumReference(
            href="https://www.redhat.com/security/data/cve/CVE-2019-5736.html",
            id="CVE-2019-5736",
            title="CVE-2019-5736",
            type="cve",
        ),
        ErratumReference(
            href="https://access.redhat.com/security/updates/classification/#important",
            id="classification",
            title="important",
            type="other",
        ),
    ]

    assert loaded.pkglist == [
        ErratumPackageCollection(
            name="collection-0",
            packages=[
                ErratumPackage(
                    arch="x86_64",
                    filename="slirp4netns-debuginfo-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.x86_64.rpm",
                    epoch="0",
                    name="slirp4netns-debuginfo",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="917ceef4aba550095d6ce5ab72b20e2e",
                    sha1sum=None,
                    sha256sum="c4de28590622f59415de3a8b9fcb427cfd34637c4a7e6accd29d3f39d7699e6d",
                ),
                ErratumPackage(
                    arch="x86_64",
                    filename="slirp4netns-debugsource-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.x86_64.rpm",
                    epoch="0",
                    name="slirp4netns-debugsource",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="9519596175f7eb90439f4f60db38e97d",
                    sha1sum=None,
                    sha256sum="d0f48388b6ba9d62d2350cd4216755f2517aaa3934663e2fc192b2f40c615e49",
                ),
                ErratumPackage(
                    arch="x86_64",
                    filename="slirp4netns-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.x86_64.rpm",
                    epoch="0",
                    name="slirp4netns",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="af0d6447dc9f81d2718e70f103070bc0",
                    sha1sum=None,
                    sha256sum="e7a6c321ae08e6050c39d5a0c94d6e765c1a9d4d2b030f219bf6d916619b29f1",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="slirp4netns-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="slirp4netns",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="c863064c1edd9f5d78208e873692c9dd",
                    sha1sum=None,
                    sha256sum="be2d49e797db6395e819335ea8debe2639d562a621c730604b38139961d9d05b",
                ),
                ErratumPackage(
                    arch="x86_64",
                    filename="skopeo-debugsource-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.x86_64.rpm",
                    epoch="1",
                    name="skopeo-debugsource",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="6ee19888b7b3f900063331c75f9c4ab6",
                    sha1sum=None,
                    sha256sum="71a82a595c93c9aef8c316fd87937e0334af51e2fc2996970ce39285daf03053",
                ),
                ErratumPackage(
                    arch="x86_64",
                    filename="skopeo-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.x86_64.rpm",
                    epoch="1",
                    name="skopeo",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="b6ae238c20daf85543d25daa292f83a7",
                    sha1sum=None,
                    sha256sum="59070bd8647cdb34f434ef1a5593ff727ab87a0df105417de0bf16a2b5232512",
                ),
                ErratumPackage(
                    arch="x86_64",
                    filename="runc-debugsource-1.0.0-55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba.x86_64.rpm",
                    epoch="0",
                    name="runc-debugsource",
                    version="1.0.0",
                    release="55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="eedf3c1be375ebbe727471f4c9a225d9",
                    sha1sum=None,
                    sha256sum="f408bd733935a79274bb810bd1cff00bca93fcfa410315b1e4f071ae177774e6",
                ),
            ],
            short="",
            module=ErratumModule(
                name="container-tools",
                stream="rhel8",
                version="8000020190416221845",
                context="2ffa3d27",
                arch="x86_64",
            ),
        ),
        ErratumPackageCollection(
            name="collection-3",
            packages=[
                ErratumPackage(
                    arch="SRPMS",
                    filename="slirp4netns-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="slirp4netns",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="c863064c1edd9f5d78208e873692c9dd",
                    sha1sum="f3d9ae4aeea6946a8668445395ba10b7399523a0",
                    sha256sum="be2d49e797db6395e819335ea8debe2639d562a621c730604b38139961d9d05b",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="skopeo-debugsource-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="skopeo-debugsource",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="76161e93a42383b4b6b1f42482f3dd4d",
                    sha1sum=None,
                    sha256sum="aea7d37b68d252d5e57d6db50b5c26188412d6464e0b81a5a6deae431ea55bee",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="skopeo-debuginfo-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="skopeo-debuginfo",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="8004f3a05e5eac46c76a2e805be3809e",
                    sha1sum=None,
                    sha256sum="dda994b3f186ed3ce6a9d7c48402a0bab7757eb020b72991c9dd35e615b5e4eb",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="runc-debugsource-1.0.0-55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba.s390x.rpm",
                    epoch="0",
                    name="runc-debugsource",
                    version="1.0.0",
                    release="55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="6b171a203c7bf91b8f0b78f453fcef9c",
                    sha1sum=None,
                    sha256sum="845de746c15d5bf7e29f5a13011066c968c1dfb05cd554b0450a2d25a7e4e3bc",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="runc-1.0.0-55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba.src.rpm",
                    epoch="0",
                    name="runc",
                    version="1.0.0",
                    release="55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="364ba52d0e1eb8fbe899c3424520eb56",
                    sha1sum=None,
                    sha256sum="3a40f68a0b93dd2ac3cddf5b1d58ef77372942777fc798ff413453d6fa0253f7",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="slirp4netns-debuginfo-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="slirp4netns-debuginfo",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="797254858bba898ace72128df8d8ec3e",
                    sha1sum=None,
                    sha256sum="e169df356459146ceaa745297d8df49a3b15cc9e648b418869ca9e35020f3cac",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="runc-1.0.0-55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba.s390x.rpm",
                    epoch="0",
                    name="runc",
                    version="1.0.0",
                    release="55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="25e8c8cd2ed9e0a0a02dc5aef09889a8",
                    sha1sum=None,
                    sha256sum="46bb4965c22bca3aadc383503a5e84d2879b19217830ee0d04f029aa0bf92f07",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="runc-debuginfo-1.0.0-55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba.s390x.rpm",
                    epoch="0",
                    name="runc-debuginfo",
                    version="1.0.0",
                    release="55.rc5.dev.git2abd837.module+el8.0.0+3049+59fd2bba",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="326c37fb3566e45dc014968e5374fa87",
                    sha1sum=None,
                    sha256sum="5db29f35f2f40cfada2231146a8f6d1e3f430722c0f8d43a2638259ff2627e3f",
                ),
                ErratumPackage(
                    arch="noarch",
                    filename="podman-docker-1.0.0-2.git921f98f.module+el8.0.0+2958+4e823551.noarch.rpm",
                    epoch="0",
                    name="podman-docker",
                    version="1.0.0",
                    release="2.git921f98f.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="ad952f9efc5f29afec5fb9530deb28b6",
                    sha1sum=None,
                    sha256sum="40d3190ed329073ed3454bb726a7452b1b3ba8cd87b7d78183e42e899d187a1d",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="podman-debugsource-1.0.0-2.git921f98f.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="podman-debugsource",
                    version="1.0.0",
                    release="2.git921f98f.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="30b56bf9f2be62a4eb2f04cb6b6fd21a",
                    sha1sum=None,
                    sha256sum="052278774a5459fea098ca1307756adf8f3039cac64aff3b8968ceb765618b09",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="podman-debuginfo-1.0.0-2.git921f98f.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="podman-debuginfo",
                    version="1.0.0",
                    release="2.git921f98f.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="1597e5db5b8b4019b3025c986286091e",
                    sha1sum=None,
                    sha256sum="af7a7ba25f770cdd7710d4fc9fbf03b9c42e48b8ec1012592a8c9dd4f67d8fa6",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="skopeo-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="1",
                    name="skopeo",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="3400331ed99d0400067f9aed159e1e0d",
                    sha1sum=None,
                    sha256sum="21dc81a5e23fee5345680ff6862536ae7390a0e9e91dba6fc667e1e60dde57d9",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="podman-1.0.0-2.git921f98f.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="podman",
                    version="1.0.0",
                    release="2.git921f98f.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="c3da563d95ae856854e0db46bd92d98b",
                    sha1sum=None,
                    sha256sum="39757bdfbe409896cff75635e3afe6aea21b25c09aab0789961d6168e8c8bff6",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="containernetworking-plugins-0.7.4-3.git9ebe139.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="containernetworking-plugins",
                    version="0.7.4",
                    release="3.git9ebe139.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="fdb5afbae0ad44795776d843f2defd76",
                    sha1sum=None,
                    sha256sum="44e465a362abb8357f2019057162d02226a510abc78c15c65a88d72c67dd53b5",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="containernetworking-plugins-0.7.4-3.git9ebe139.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="containernetworking-plugins",
                    version="0.7.4",
                    release="3.git9ebe139.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="cc9e5527550ebf573ad36c5092c19ffc",
                    sha1sum=None,
                    sha256sum="b212c36df71a20689079592f27a9d03870a623a11f51a9761f7973e659939f81",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="containernetworking-plugins-debugsource-0.7.4-3.git9ebe139.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="containernetworking-plugins-debugsource",
                    version="0.7.4",
                    release="3.git9ebe139.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="85a20df93f2b529ad239e00492b67cd7",
                    sha1sum=None,
                    sha256sum="3a0b84d25293ede8957c38dae236947cd508415a7f0b892ad205d8cdb37f35e1",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="2",
                    name="container-selinux",
                    version="2.94",
                    release="1.git1e99f1d.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="e4265aa655362fdf6cc0265a29dc3792",
                    sha1sum=None,
                    sha256sum="e014ffe8047a36c08ddfdaa4f96a09d954cef60c17c2c79a6dc0d72d4ba5770e",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="skopeo-0.1.32-3.git1715c90.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="skopeo",
                    version="0.1.32",
                    release="3.git1715c90.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="d382120e5fdaaa24e405fbb5ee670451",
                    sha1sum=None,
                    sha256sum="501765be7912c9d08ab5c5f5752ecf73569536457cd3ee2ce0643f70d3991cde",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="podman-1.0.0-2.git921f98f.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="podman",
                    version="1.0.0",
                    release="2.git921f98f.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="69ce75e8b3f2a2271cd8f17b6b1db4b7",
                    sha1sum=None,
                    sha256sum="893044e6293c97fd33e55d57058505b012d5aada5ebfc25cc00aa6950160cd84",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="buildah-1.5-3.gite94b4f9.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="buildah",
                    version="1.5",
                    release="3.gite94b4f9.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="d63e2bc9c179ea8135b9fc7ce8f4e326",
                    sha1sum=None,
                    sha256sum="044fd3ab6a4231843c704998b61eb161839ae0c203ed2b0a9cbe0259f35bc65b",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="slirp4netns-debugsource-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="slirp4netns-debugsource",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="c2e8d125a5e2c65fef41cca893048400",
                    sha1sum=None,
                    sha256sum="a85891d07733c3e7b765229358d2cec33331731649265a105a7b742e5b0accfa",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="fuse-overlayfs-0.3-2.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="fuse-overlayfs",
                    version="0.3",
                    release="2.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="b09d3edcc9350a269b6c4c4c277d270a",
                    sha1sum=None,
                    sha256sum="88c203351d6aae3f5a02ea46fc221be18d28e3c3f2c5ebd17bada049bdb9e4d8",
                ),
                ErratumPackage(
                    arch="noarch",
                    filename="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.noarch.rpm",
                    epoch="2",
                    name="container-selinux",
                    version="2.94",
                    release="1.git1e99f1d.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="f7d31e5f099bcdadf419239db840baa8",
                    sha1sum=None,
                    sha256sum="8a3a4eb8c3ee529e3b103ece6200517ff6834d24dab1d202e392347efedc254e",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="containernetworking-plugins-debuginfo-0.7.4-3.git9ebe139.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="containernetworking-plugins-debuginfo",
                    version="0.7.4",
                    release="3.git9ebe139.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="da26f260ae089792ec07a876f4dbf2bb",
                    sha1sum=None,
                    sha256sum="e78ffa580ea6daad1fd16c15aa3483f2d85f0c15d6ba23c4a372daaa4382e31f",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="buildah-1.5-3.gite94b4f9.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="0",
                    name="buildah",
                    version="1.5",
                    release="3.gite94b4f9.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="d2366a6349f28506bfd4fb0525b533d7",
                    sha1sum=None,
                    sha256sum="55756e48575e8cf7eab5021c8ecd788e66741287a6da6d4dc18ed005e22e3093",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="buildah-debuginfo-1.5-3.gite94b4f9.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="buildah-debuginfo",
                    version="1.5",
                    release="3.gite94b4f9.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="4c8460d1f71c6d574aeca973ad2e0d89",
                    sha1sum=None,
                    sha256sum="65c626e0d15440fb56e8e0489da3f1ccf1442f3ba6ebf3338eefdf7ee98cea89",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="slirp4netns-0.1-2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="slirp4netns",
                    version="0.1",
                    release="2.dev.gitc4e1bc5.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="41cec16504692c5bc462b7d5f8737087",
                    sha1sum=None,
                    sha256sum="0e9580680295adeba3bc9f033176492f881adb98cbe919b921b9ec9a74f80181",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="fuse-overlayfs-debuginfo-0.3-2.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="fuse-overlayfs-debuginfo",
                    version="0.3",
                    release="2.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="51c4b466077a37084d7fedfdda3f57ff",
                    sha1sum=None,
                    sha256sum="fddcdcf52fec789deb0d68d871cc3e9960ec4f1f0930c3275f188b5a968d93d1",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="fuse-overlayfs-debugsource-0.3-2.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="fuse-overlayfs-debugsource",
                    version="0.3",
                    release="2.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="ba7f2bac9de2bdf232187b9c543c47fc",
                    sha1sum=None,
                    sha256sum="c7b0b7de23a900d05fe4052614e68226b00f1252b505898e14da3382002c26ef",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="oci-systemd-hook-0.1.15-2.git2d0b8a3.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="oci-systemd-hook",
                    version="0.1.15",
                    release="2.git2d0b8a3.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="122fc1079f4a05e0b2dee5e60dea3e54",
                    sha1sum=None,
                    sha256sum="593595e3005ea32cf2ca84c93e1cba832461b2854b003046f3bd59f2e331819b",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="fuse-overlayfs-0.3-2.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="0",
                    name="fuse-overlayfs",
                    version="0.3",
                    release="2.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="5eeec013645c903124089ceae13e6710",
                    sha1sum=None,
                    sha256sum="28211a39e8bbdaf8792fc4485699696e67f62a0c4a40fc22a9ac1b7399f8edf7",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="oci-systemd-hook-0.1.15-2.git2d0b8a3.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="1",
                    name="oci-systemd-hook",
                    version="0.1.15",
                    release="2.git2d0b8a3.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="a338cf74fe10bce021bbd5d8ba335657",
                    sha1sum=None,
                    sha256sum="e7c95270d345a04b03d9f2351aca6f2f298764a89bf2039b27de71adc1362f8c",
                ),
                ErratumPackage(
                    arch="SRPMS",
                    filename="oci-umount-2.3.4-2.git87f9237.module+el8.0.0+2958+4e823551.src.rpm",
                    epoch="2",
                    name="oci-umount",
                    version="2.3.4",
                    release="2.git87f9237.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="aa746cb0a01066d7fa670ca420833cf0",
                    sha1sum=None,
                    sha256sum="eeb07a3822a3a4e4f78dd94e0e34a3b227d7d17d87ea04267439eb27c2265b33",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="oci-systemd-hook-debuginfo-0.1.15-2.git2d0b8a3.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="oci-systemd-hook-debuginfo",
                    version="0.1.15",
                    release="2.git2d0b8a3.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="a55e75853de831fec4462adf79257a03",
                    sha1sum=None,
                    sha256sum="e01939fdfa24a707ed422262bb19a68e5e22995afd0f669be06c33202e00847a",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="oci-systemd-hook-debugsource-0.1.15-2.git2d0b8a3.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="1",
                    name="oci-systemd-hook-debugsource",
                    version="0.1.15",
                    release="2.git2d0b8a3.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="9b29f218aac3861685faff8c69bb03ac",
                    sha1sum=None,
                    sha256sum="c55dfc5af5c4a715f69b95a3772a4ede50db2d78c88cc9ca00b271d9f8b0c4a4",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="oci-umount-debuginfo-2.3.4-2.git87f9237.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="2",
                    name="oci-umount-debuginfo",
                    version="2.3.4",
                    release="2.git87f9237.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="1f891c443aa35396dd57ae1185f98f9c",
                    sha1sum=None,
                    sha256sum="344385d9c0cfdca4ddf16876936e36abad91c1cd7b99d3cb86e2fc5f858cb56f",
                ),
                ErratumPackage(
                    arch="s390x",
                    filename="oci-umount-2.3.4-2.git87f9237.module+el8.0.0+2958+4e823551.s390x.rpm",
                    epoch="2",
                    name="oci-umount",
                    version="2.3.4",
                    release="2.git87f9237.module+el8.0.0+2958+4e823551",
                    src="container-selinux-2.94-1.git1e99f1d.module+el8.0.0+2958+4e823551.src.rpm",
                    reboot_suggested=None,
                    md5sum="eba982381b3a54d0ae7c14230f29fd69",
                    sha1sum=None,
                    sha256sum="872610d40f5f50030ef6188d26178ae7b0dc8eedab72e285c8b513f8df145a2b",
                ),
            ],
            short="",
            module=ErratumModule(
                name="container-tools",
                stream="rhel8",
                version="8000020190416221845",
                context="2ffa3d27",
                arch="s390x",
            ),
        ),
    ]

    loaded = attr.evolve(loaded, pkglist=[], references=[])

    assert loaded == ErratumUnit(
        unit_id="d003313d-2272-4ba3-8ea9-820269284dc2",
        id="RHSA-2019:0975",
        version="1",
        status="final",
        updated="2019-05-07 03:39:02 UTC",
        issued="2019-05-07 03:39:11 UTC",
        description="The container-tools module contains tools for working with containers, notably podman, buildah, skopeo, and runc.\n\nSecurity Fix(es):\n\n* A flaw was found in the way runc handled system file descriptors when running containers. A malicious container could use this flaw to overwrite contents of the runc binary and consequently run arbitrary commands on the container host system. (CVE-2019-5736)\n\nFor more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.\n\nBug Fix(es):\n\n* [stream rhel8] rebase container-selinux to 2.94 (BZ#1693675)\n\n* [stream rhel8] unable to mount disk at `/var/lib/containers` via `systemd` unit when `container-selinux` policy installed (BZ#1695669)\n\n* [stream rhel8] don't allow a container to connect to random services (BZ#1695689)",
        pushcount="8",
        reboot_suggested=False,
        from_="noreply@example.com",
        rights="Copyright 2019 Red Hat Inc",
        title="Important: container-tools:rhel8 security and bug fix update",
        severity="Important",
        release="0",
        type="security",
        solution="For details on how to apply this update, which includes the changes described in this advisory, refer to:\n\nhttps://access.redhat.com/articles/11258",
        summary="An update for the container-tools:rhel8 module is now available for Red Hat Enterprise Linux 8.\n\nRed Hat Product Security has rated this update as having a security impact of Important. A Common Vulnerability Scoring System (CVSS) base score, which gives a detailed severity rating, is available for each vulnerability from the CVE link(s) in the References section.",
        content_types=["module"],
        references=[],
        pkglist=[],
        content_type_id="erratum",
        container_list=[
            {
              "e2e/test-operator-container": {
                "digest": "sha256:2321a7d13d9fa53f05437663cf2dc217d15f3cda4b67076c941b10f0491cf9d7",
                "images": {
                  "docker-image-sha256:06d1c5e4fa6a5d1ff868388f3feadf193d04128b62d1181e37fe4ab8ecda27e1.s390x.tar.gz": {
                    "digest": None
                  },
                  "docker-image-sha256:05649a19718fde131372c761d359302ccbe81f9744d2893ac4c826b05d670206.ppc64le.tar.gz": {
                    "digest": None
                  },
                  "docker-image-sha256:c2e3030306f71b94cbffe2d16fcebe6e14f2842ae26789926bcf1afeeecb5859.x86_64.tar.gz": {
                    "digest": None
                  }
                }
              }
            }

        ],
        repository_memberships=[
            "all-rpm-content",
            "rhel-8-for-aarch64-appstream-source-rpms__8_DOT_0",
            "rhel-8-for-aarch64-appstream-source-rpms__8_DOT_1",
            "rhel-8-for-aarch64-appstream-source-rpms__8_DOT_2",
            "rhel-8-for-aarch64-appstream-source-rpms__8_DOT_3",
            "rhel-8-for-ppc64le-appstream-rpms__8_DOT_0",
            "rhel-8-for-ppc64le-appstream-rpms__8_DOT_1",
            "rhel-8-for-ppc64le-appstream-rpms__8_DOT_2",
            "rhel-8-for-ppc64le-appstream-rpms__8_DOT_3",
            "rhel-8-for-s390x-appstream-rpms__8",
            "rhel-8-for-s390x-appstream-rpms__8_DOT_1",
            "rhel-8-for-s390x-appstream-rpms__8_DOT_2",
            "rhel-8-for-x86_64-appstream-rpms__8",
        ],
    )
