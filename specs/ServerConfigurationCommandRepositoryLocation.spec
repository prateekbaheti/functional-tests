// --GO-LICENSE-START--
// Copyright 2015 ThoughtWorks, Inc.
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//    http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// --GO-LICENSE-END--

ServerConfigurationCommandRepositoryLocation
============================================

Setup of contexts
* Basic configuration - setup
* Capture go state "ServerConfigurationCommandRepositoryLocation" - setup
* Setup command repo - setup

ServerConfigurationCommandRepositoryLocation
--------------------------------------------

tags: 6664, admin-page, configuration, task-repository-location

* Open "Server Configuration" tab

* Verify command repository location is set to "default"

* Using "." as command repository location
* Save configuration
* Verify message contains "Failed to save the server configuration. Reason: Invalid Repository Location, repository should be a subdirectory under"

* Using "custom" as command repository location
* Save configuration
* Verify message "Saved configuration successfully." shows up





Teardown of contexts
* Setup command repo - teardown
* Capture go state "ServerConfigurationCommandRepositoryLocation" - teardown
* Basic configuration - teardown


