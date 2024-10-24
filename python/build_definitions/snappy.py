#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

import subprocess

from yugabyte_db_thirdparty.build_definition_helpers import *  # noqa


class SnappyDependency(Dependency):
    def __init__(self) -> None:
        super(SnappyDependency, self).__init__(
            name='snappy',
            version='1.1.9-yb-3',
            url_pattern='https://github.com/yugabyte/snappy/archive/refs/tags/v{0}.tar.gz',
            build_group=BUILD_GROUP_INSTRUMENTED)

    def build(self, builder: BuilderInterface) -> None:
        builder.build_with_cmake(
            dep=self,
            extra_args=[
                '-DSNAPPY_BUILD_TESTS=OFF',
                '-DSNAPPY_BUILD_BENCHMARKS=OFF',
            ],
            shared_and_static=True
        )
