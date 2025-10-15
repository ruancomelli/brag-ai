# Changelog

## [0.1.4](https://github.com/ruancomelli/brag-ai/compare/v0.1.3..v0.1.4) - 2025-10-15

### ✨ Features

- *(cli)* Display the required API key envvar in `ls-models` ([#87](https://github.com/ruancomelli/brag-ai/issues/87)) - ([24961f2](https://github.com/ruancomelli/brag-ai/commit/24961f26de7e0e80ada0b3f55d425e805061dac3))
- *(models)* Add token-counting ability ([#58](https://github.com/ruancomelli/brag-ai/issues/58)) - ([8989125](https://github.com/ruancomelli/brag-ai/commit/8989125e54dbabf03a313c8c265044f3f3be3d33))
- Add support for `anthropic:claude-3-7-sonnet` ([#84](https://github.com/ruancomelli/brag-ai/issues/84)) - ([cb8a967](https://github.com/ruancomelli/brag-ai/commit/cb8a967cecc04c27ce13902d8575e030a218dac5))
- Add support for updating an existing brag document ([#67](https://github.com/ruancomelli/brag-ai/issues/67)) - ([d3df151](https://github.com/ruancomelli/brag-ai/commit/d3df151531768e6c7791a133d28f51311b885b8e))
- Add `from-local` command to generate brag documents from local repositories ([#64](https://github.com/ruancomelli/brag-ai/issues/64)) - ([3d7c9c9](https://github.com/ruancomelli/brag-ai/commit/3d7c9c9785dceeef0aba89df9c4450a8a83aa226))
- Accept full GitHub URLs in addition to `owner/repo` strings ([#63](https://github.com/ruancomelli/brag-ai/issues/63)) - ([28377bf](https://github.com/ruancomelli/brag-ai/commit/28377bf67af6cbaa77cf317ee4dc9ed545304c69))
- Add Docker support ([#60](https://github.com/ruancomelli/brag-ai/issues/60)) - ([c9ed15c](https://github.com/ruancomelli/brag-ai/commit/c9ed15c7927270893a0ede6af2927875fe5f0305))
- Batch commits during brag document generation ([#59](https://github.com/ruancomelli/brag-ai/issues/59)) - ([d145267](https://github.com/ruancomelli/brag-ai/commit/d145267309b7a0fdd4fc942be063cea5119014eb))

### 🐛 Bug Fixes

- *(agents)* Emphasize ability to modify the existing brag document in prompt ([#86](https://github.com/ruancomelli/brag-ai/issues/86)) - ([5f81bb9](https://github.com/ruancomelli/brag-ai/commit/5f81bb9a82e9f90649b5108b442f9dd7881ae6b1))
- *(cli/self)* Install the `brag-ai` project instead of trying to install `brag` ([#65](https://github.com/ruancomelli/brag-ai/issues/65)) - ([60f0fb9](https://github.com/ruancomelli/brag-ai/commit/60f0fb9564c8d148eff924379ba456ffcc3e7097))
- *(sources/github_commits)* Handle empty file patches ([#85](https://github.com/ruancomelli/brag-ai/issues/85)) - ([618d62c](https://github.com/ruancomelli/brag-ai/commit/618d62c7a3b33773f0635e186c7c03296e7e8ced))

### 🔧 Chores

- Switch to MIT license ([#102](https://github.com/ruancomelli/brag-ai/issues/102)) - ([45aff0e](https://github.com/ruancomelli/brag-ai/commit/45aff0ee3c28d916f88949e3719f2b21f3000a1a))
- Improve Trove classifiers based on the official list on PyPI ([#95](https://github.com/ruancomelli/brag-ai/issues/95)) - ([56836db](https://github.com/ruancomelli/brag-ai/commit/56836dbaba70fa2893752e15c97c2e7cf4e45b8f))
- Add LICENSE metadata to `pyproject.toml` ([#94](https://github.com/ruancomelli/brag-ai/issues/94)) - ([301cf1a](https://github.com/ruancomelli/brag-ai/commit/301cf1a34d5decf1adee238ffbd384fe639fe609))
- Add a `py.typed` file to let dependendants know that the project is typed ([#82](https://github.com/ruancomelli/brag-ai/issues/82)) - ([fecfe77](https://github.com/ruancomelli/brag-ai/commit/fecfe77beae03605bf9baf102b044c5f46a54b6b))
- Add LICENSE ([#74](https://github.com/ruancomelli/brag-ai/issues/74)) - ([3e60731](https://github.com/ruancomelli/brag-ai/commit/3e6073110eec455f7c91308b4cdce0448eae4b0f))

### 📚 Documentation

- *(README)* Remove commented-out license badge ([#97](https://github.com/ruancomelli/brag-ai/issues/97)) - ([ae2be87](https://github.com/ruancomelli/brag-ai/commit/ae2be8730e9875258273508be508f86369b4ce62))
- *(README)* Include `.git` suffix in the link to the repository ([#89](https://github.com/ruancomelli/brag-ai/issues/89)) - ([6f31e27](https://github.com/ruancomelli/brag-ai/commit/6f31e27a8791683f496c2aad422ba2d86b2d4634))
- *(README)* Prompt users to star the project ([#51](https://github.com/ruancomelli/brag-ai/issues/51)) - ([7fc7214](https://github.com/ruancomelli/brag-ai/commit/7fc72145b3ef0b84eaef61c254257f8ef8f1de44))
- *(README)* Add basic project badges ([#47](https://github.com/ruancomelli/brag-ai/issues/47)) - ([60757b7](https://github.com/ruancomelli/brag-ai/commit/60757b76be755ed893d6dca1000c9f07dfa2318f))
- Update domain name of the docs ([#92](https://github.com/ruancomelli/brag-ai/issues/92)) - ([3780d82](https://github.com/ruancomelli/brag-ai/commit/3780d829bb0282d89c1cf812603efa4285fcc6eb))
- Remove unnecessary fields from `mkdocs.yml` ([#70](https://github.com/ruancomelli/brag-ai/issues/70)) - ([0589b06](https://github.com/ruancomelli/brag-ai/commit/0589b060f6b93343bb1000e893cd52abff71e257))
- Fix copyright year to be 2025 ([#96](https://github.com/ruancomelli/brag-ai/issues/96)) - ([0caa67d](https://github.com/ruancomelli/brag-ai/commit/0caa67de7c0af5eedce970a787572e692241fbec))
- Fix docs now that we need to call `brag from-repo` ([#57](https://github.com/ruancomelli/brag-ai/issues/57)) - ([e60a219](https://github.com/ruancomelli/brag-ai/commit/e60a2199b8e2f818ad2dd1a6780af9b9827df9cc))
- Improve the hero and add a favicon icon ([#55](https://github.com/ruancomelli/brag-ai/issues/55)) - ([2c3065f](https://github.com/ruancomelli/brag-ai/commit/2c3065f40518d2b74c7c5e0233f9498b26e656fc))
- Generate API reference docs automatically ([#48](https://github.com/ruancomelli/brag-ai/issues/48)) - ([70f4375](https://github.com/ruancomelli/brag-ai/commit/70f4375ae84dc8822884f4532af1fa52ddebfeb9))
- Update docs after publishing project to PyPI ([#46](https://github.com/ruancomelli/brag-ai/issues/46)) - ([3caabb1](https://github.com/ruancomelli/brag-ai/commit/3caabb1962e2a0a6c808c020d2aea9d6a713f747))

### ♻️ Refactor

- *(batching)* Improve variable naming to avoid confusion ([#113](https://github.com/ruancomelli/brag-ai/issues/113)) - ([3277900](https://github.com/ruancomelli/brag-ai/commit/327790018c36883f92301f44203df577b1a19a8f))
- *(cli)* Track progress consistently in the CLI ([#88](https://github.com/ruancomelli/brag-ai/issues/88)) - ([e7da402](https://github.com/ruancomelli/brag-ai/commit/e7da402e7b2d52ea5bd4c53e4c06f37eafc9c6a9))
- *(cli)* Use Markdown rendering for the help texts ([#99](https://github.com/ruancomelli/brag-ai/issues/99)) - ([7927b13](https://github.com/ruancomelli/brag-ai/commit/7927b13ab7b27367c3908488f458f587ee01da3c))
- *(cli)* Remove unused and untested `self` subcommand ([#66](https://github.com/ruancomelli/brag-ai/issues/66)) - ([56de459](https://github.com/ruancomelli/brag-ai/commit/56de459c83489c3692193bf9ad961a14dfb88365))
- Replace `typer` with `cryclopts` ([#56](https://github.com/ruancomelli/brag-ai/issues/56)) - ([03d4fe9](https://github.com/ruancomelli/brag-ai/commit/03d4fe948e60efe6078c1387fd230ec8201968d3))

### 🎨 Styling

- Pretty format `.github/git-cliff-config.toml` ([#81](https://github.com/ruancomelli/brag-ai/issues/81)) - ([af4f8de](https://github.com/ruancomelli/brag-ai/commit/af4f8de832d19f2765a5c926767418feaa56d8a0))

### 🏗️ Build System

- Replace `pydantic-ai` with `pydantic-ai-slim` for a smaller dependency chain ([#83](https://github.com/ruancomelli/brag-ai/issues/83)) - ([9e096bd](https://github.com/ruancomelli/brag-ai/commit/9e096bdb7edf7f34be8d8110332f6298a443811a))

### 🔄 CI/CD

- Only run `semantic-pull-request-title` workflow when the PR title changes ([#101](https://github.com/ruancomelli/brag-ai/issues/101)) - ([54454ff](https://github.com/ruancomelli/brag-ai/commit/54454ffe888c912d89d586fa3a8747d171b49177))
- Bump `uv-pre-commit` version ([#93](https://github.com/ruancomelli/brag-ai/issues/93)) - ([15e1106](https://github.com/ruancomelli/brag-ai/commit/15e11068c1a66974c444715c75737ac19d56bd62))
- Disable `pre-commit-check` in CI checks ([#90](https://github.com/ruancomelli/brag-ai/issues/90)) - ([9be7c83](https://github.com/ruancomelli/brag-ai/commit/9be7c836553420224e7fb56ecf5abe51a5087f2e))
- Enable strict checks for MyPy ([#78](https://github.com/ruancomelli/brag-ai/issues/78)) - ([7e421ac](https://github.com/ruancomelli/brag-ai/commit/7e421aca139edb6cbdfba41efb5af37294ffcffc))
- Run all pre-commit checks in CI ([#77](https://github.com/ruancomelli/brag-ai/issues/77)) - ([cc3f763](https://github.com/ruancomelli/brag-ai/commit/cc3f76392a32f991c64b5a01914ad9e33c5cb0c3))
- Pretty-format TOML files ([#76](https://github.com/ruancomelli/brag-ai/issues/76)) - ([0d5002e](https://github.com/ruancomelli/brag-ai/commit/0d5002e894c7e12446f06949c9b785cbf9ba1891))
- Add `deptry` to pre-commit checks ([#75](https://github.com/ruancomelli/brag-ai/issues/75)) - ([8effe36](https://github.com/ruancomelli/brag-ai/commit/8effe36950c4a7f563d93865150840b436ecfbc7))
- Fix CodeFlash usage in GitHub Actions ([#80](https://github.com/ruancomelli/brag-ai/issues/80)) - ([f790f48](https://github.com/ruancomelli/brag-ai/commit/f790f483fec11e69f05332ddb466abe52b41e832))
- Add CodeFlash AI to CI workflows ([#72](https://github.com/ruancomelli/brag-ai/issues/72)) - ([c357da6](https://github.com/ruancomelli/brag-ai/commit/c357da665105a057146c4ad89a6cd85477ddc5df))
- Publish project to PyPI in the same job that we release ([#68](https://github.com/ruancomelli/brag-ai/issues/68)) - ([7febd26](https://github.com/ruancomelli/brag-ai/commit/7febd26671d3b45484c79ffb6e9c63396de01c0a))

### 📦 Dependencies

- *(deps)* Bump Rich version to support Python 3.14 ([#115](https://github.com/ruancomelli/brag-ai/issues/115)) - ([fe66577](https://github.com/ruancomelli/brag-ai/commit/fe665772e88710efac76c7c5d4413c3b4852e5eb))
- *(deps)* Update actions/checkout action to v5 ([#103](https://github.com/ruancomelli/brag-ai/issues/103)) - ([34339c1](https://github.com/ruancomelli/brag-ai/commit/34339c19b3f17d808da2de6d4aa503bc72054917))
- *(deps)* Update github/codeql-action action to v4 ([#106](https://github.com/ruancomelli/brag-ai/issues/106)) - ([9162dd8](https://github.com/ruancomelli/brag-ai/commit/9162dd81d99ed6201cb7bb33d1c0215a018a6246))
- *(deps)* Update amannn/action-semantic-pull-request action to v6 ([#104](https://github.com/ruancomelli/brag-ai/issues/104)) - ([11fff13](https://github.com/ruancomelli/brag-ai/commit/11fff1356c3d1f63feb8018ad153d88ba278f768))
- *(deps)* Update actions/upload-pages-artifact action to v4 ([#105](https://github.com/ruancomelli/brag-ai/issues/105)) - ([f443918](https://github.com/ruancomelli/brag-ai/commit/f44391836fa18f640e41fa5a64074b3830c1f0aa))
- *(deps)* Update astral-sh/setup-uv action to v7 ([#108](https://github.com/ruancomelli/brag-ai/issues/108)) - ([c9fc7fa](https://github.com/ruancomelli/brag-ai/commit/c9fc7fa5b07cd73f770c15cf260bef009d156673))
- *(deps)* Update astral-sh/setup-uv action to v6 ([#100](https://github.com/ruancomelli/brag-ai/issues/100)) - ([5ed3196](https://github.com/ruancomelli/brag-ai/commit/5ed31966a3459e8fa7b521e521c2bb6f1d0530c0))
- *(deps)* Update astral-sh/setup-uv action to v5 ([#73](https://github.com/ruancomelli/brag-ai/issues/73)) - ([efe3f5d](https://github.com/ruancomelli/brag-ai/commit/efe3f5dd69549df500ec2356337ed551102cc97f))

## New Contributors ❤️

* @saumya4751 made their first contribution in [#60](https://github.com/ruancomelli/brag-ai/pull/60)## [0.1.3](https://github.com/ruancomelli/brag-ai/compare/vv0.1.2..v0.1.3) - 2025-03-07

### 🐛 Bug Fixes

- *(release)* Remove extra leading `v`s in version tag ([#45](https://github.com/ruancomelli/brag-ai/issues/45)) - ([205e7c4](https://github.com/ruancomelli/brag-ai/commit/205e7c434621d0576834ccdb37cd62932315cb4f))

### 🔧 Chores

- Release v0.1.3 - ([7c42d86](https://github.com/ruancomelli/brag-ai/commit/7c42d86407b40456835c236b752c15b048bf5517))
- Add documentation and changelog URLs to project URLs ([#44](https://github.com/ruancomelli/brag-ai/issues/44)) - ([e697335](https://github.com/ruancomelli/brag-ai/commit/e6973354da681ffbfc6e4d175282472cd5e7f23c))
- Fix project name from `brag` to `brag-ai` ([#43](https://github.com/ruancomelli/brag-ai/issues/43)) - ([2364bd5](https://github.com/ruancomelli/brag-ai/commit/2364bd50ca395721149a56b591df5e58a27e1328))
## [0.1.2](https://github.com/ruancomelli/brag-ai/compare/vv0.1.1..vv0.1.2) - 2025-03-06

### 🐛 Bug Fixes

- *(release)* Correctly dispatch the `publish` workflow after the `release` ([#42](https://github.com/ruancomelli/brag-ai/issues/42)) - ([935d6f0](https://github.com/ruancomelli/brag-ai/commit/935d6f0a656a095277162eb01bffaa0c213377b1))

### 🔧 Chores

- Release vv0.1.2 - ([342e061](https://github.com/ruancomelli/brag-ai/commit/342e061a953659f6fc72bba1d49e08eb66dc0d75))
## [0.1.1](https://github.com/ruancomelli/brag-ai/compare/v0.1.0..vv0.1.1) - 2025-03-06

### 🐛 Bug Fixes

- *(release)* Use the actor name provided by the `github` environment ([#41](https://github.com/ruancomelli/brag-ai/issues/41)) - ([b578347](https://github.com/ruancomelli/brag-ai/commit/b578347544db77d4711dd54abe01137befd1859d))

### 🔧 Chores

- Release vv0.1.1 - ([4d80e4d](https://github.com/ruancomelli/brag-ai/commit/4d80e4d05b654051dea1bbee9e39307ece8c56c5))
## [0.1.0] - 2025-03-06

### ✨ Features

- Implement initial version of the script ([#4](https://github.com/ruancomelli/brag-ai/issues/4)) - ([d24f22a](https://github.com/ruancomelli/brag-ai/commit/d24f22a42f7d04fc877041048b86f69e2ad426c9))
- Implement initial working structure for the project - ([0c8c0b0](https://github.com/ruancomelli/brag-ai/commit/0c8c0b0b75d65172fec646c1636a6b9a39024807))

### 🐛 Bug Fixes

- *(release)* Add PAT to bypass `main` protection rules ([#40](https://github.com/ruancomelli/brag-ai/issues/40)) - ([d4c3405](https://github.com/ruancomelli/brag-ai/commit/d4c3405f4a45bb255b8e3bdf43159fd921242be1))
- *(release)* Use my own e-mail to commit ([#39](https://github.com/ruancomelli/brag-ai/issues/39)) - ([22e785b](https://github.com/ruancomelli/brag-ai/commit/22e785bfe5a79f637148e685cfd84ffb369baf33))
- *(release)* Set remote URL for pushing changes in workflow ([#38](https://github.com/ruancomelli/brag-ai/issues/38)) - ([e740bb4](https://github.com/ruancomelli/brag-ai/commit/e740bb4ed291c36b9a17db0fe4ca0e3d2fcdf6f1))
- *(release)* Use the `github-actions` bot e-mail to commit ([#37](https://github.com/ruancomelli/brag-ai/issues/37)) - ([07f7c06](https://github.com/ruancomelli/brag-ai/commit/07f7c06cc06d50c052260e2d6321bfffc4517d2d))
- *(release)* Correctly use the input version ([#36](https://github.com/ruancomelli/brag-ai/issues/36)) - ([086dd1e](https://github.com/ruancomelli/brag-ai/commit/086dd1e5e6a6931747b94daa1b90537ae9f5440a))
- *(release)* Configure git user and e-mail for pushing changes ([#35](https://github.com/ruancomelli/brag-ai/issues/35)) - ([6bef4ae](https://github.com/ruancomelli/brag-ai/commit/6bef4aee13d35bbcb61b3089bb7cd32792607df6))

### 🔧 Chores

- Release v0.1.0 - ([e1d03ec](https://github.com/ruancomelli/brag-ai/commit/e1d03ec9a29429dffe41a44160d7202093843bfe))
- Enhance issue templates ([#25](https://github.com/ruancomelli/brag-ai/issues/25)) - ([9e78e52](https://github.com/ruancomelli/brag-ai/commit/9e78e52cc7834ad4e6631d5cd197220f35b8a497))
- Add "internal improvement" issue template ([#23](https://github.com/ruancomelli/brag-ai/issues/23)) - ([ee943e1](https://github.com/ruancomelli/brag-ai/commit/ee943e166d0a28a0426faaa7c7167a60d8037766))
- Add default issue templates ([#20](https://github.com/ruancomelli/brag-ai/issues/20)) - ([d1832c5](https://github.com/ruancomelli/brag-ai/commit/d1832c5adcf75c6e62fd0d8e908286406f4502da))

### 📚 Documentation

- *(README)* Add hero image ([#17](https://github.com/ruancomelli/brag-ai/issues/17)) - ([cf0e21d](https://github.com/ruancomelli/brag-ai/commit/cf0e21ddf7d3a25c356fd2d25eddef7b4d6a0c46))
- *(README)* Tweak README to be more playful ([#5](https://github.com/ruancomelli/brag-ai/issues/5)) - ([ba6fbff](https://github.com/ruancomelli/brag-ai/commit/ba6fbff09db92b449f8454b333ed33e9107f1b2f))
- Simplify `README.md` and revamp `CONTRIBUTING.md` ([#31](https://github.com/ruancomelli/brag-ai/issues/31)) - ([2a7118b](https://github.com/ruancomelli/brag-ai/commit/2a7118bbf84b5f7a0f238e1e9c34c81d6ef973ae))
- Publish docs to GitHub pages ([#30](https://github.com/ruancomelli/brag-ai/issues/30)) - ([c9efad9](https://github.com/ruancomelli/brag-ai/commit/c9efad99c4546f43acf370624bba1db70bd277c3))
- Add CONTRIBUTING.md ([#15](https://github.com/ruancomelli/brag-ai/issues/15)) - ([22ec861](https://github.com/ruancomelli/brag-ai/commit/22ec861153c33146434db9be019776dbfa1be657))

### ♻️ Refactor

- *(cli)* Add progress tracking to each consumed commit ([#22](https://github.com/ruancomelli/brag-ai/issues/22)) - ([18e80bf](https://github.com/ruancomelli/brag-ai/commit/18e80bf284870bc335f509cf9762631f6765887d))
- Replace `dedent_triple_quote_string` with `promptify` ([#11](https://github.com/ruancomelli/brag-ai/issues/11)) - ([68c23ad](https://github.com/ruancomelli/brag-ai/commit/68c23ad489ffe9a3d39ca1061975495b3c2b7b5f))
- Replace custom `asyncio` module with `asyncer` library ([#10](https://github.com/ruancomelli/brag-ai/issues/10)) - ([699613a](https://github.com/ruancomelli/brag-ai/commit/699613a324dea172e35c65b4fe13e5dd7e7b1726))

### 🧪 Testing

- Add tests for `repository` ([#9](https://github.com/ruancomelli/brag-ai/issues/9)) - ([b2ab210](https://github.com/ruancomelli/brag-ai/commit/b2ab21092180451f0eab9edd6814a9c8a4623b14))
- Add tests for `text_formatters` ([#8](https://github.com/ruancomelli/brag-ai/issues/8)) - ([693d54a](https://github.com/ruancomelli/brag-ai/commit/693d54a33e00a299341e3774bc3763fed35f2a9c))

### 🏗️ Build System

- Drop support for Python 3.11 ([#21](https://github.com/ruancomelli/brag-ai/issues/21)) - ([0334bdf](https://github.com/ruancomelli/brag-ai/commit/0334bdfa6b06c991e8d6061564ab71a702f6534f))
- Set the project version in `src/brag/__init__.py` ([#12](https://github.com/ruancomelli/brag-ai/issues/12)) - ([3e2ec68](https://github.com/ruancomelli/brag-ai/commit/3e2ec687a1da36ece2835d74a51de65593fb26a1))

### 🔄 CI/CD

- Add workflow for releasing a new version ([#32](https://github.com/ruancomelli/brag-ai/issues/32)) - ([bfde8c6](https://github.com/ruancomelli/brag-ai/commit/bfde8c6841f045bad8a5f2d1f553337f09101262))
- Add zizmor to CI ([#29](https://github.com/ruancomelli/brag-ai/issues/29)) - ([9adb47b](https://github.com/ruancomelli/brag-ai/commit/9adb47b972d7b167e579aba58429d98364187b82))
- Add ActionLint to CI ([#28](https://github.com/ruancomelli/brag-ai/issues/28)) - ([273e109](https://github.com/ruancomelli/brag-ai/commit/273e109a6f2168b471d23d6e18c8da2e7bd986e7))
- Add ShellCheck to CI ([#27](https://github.com/ruancomelli/brag-ai/issues/27)) - ([cfcd081](https://github.com/ruancomelli/brag-ai/commit/cfcd0812b4198f00df676e048f58649962ca2492))
- Check semantic PR titles ([#19](https://github.com/ruancomelli/brag-ai/issues/19)) - ([64fb6e4](https://github.com/ruancomelli/brag-ai/commit/64fb6e40fb89569ca573382d34bda461c25627d1))
- Fix test coverage checks and upload to CodeCov ([#18](https://github.com/ruancomelli/brag-ai/issues/18)) - ([e2db2a4](https://github.com/ruancomelli/brag-ai/commit/e2db2a445e6f2aef060e58439ba0b97ce49cd142))
- Replace `nox` with custom scripts ([#16](https://github.com/ruancomelli/brag-ai/issues/16)) - ([185f1b8](https://github.com/ruancomelli/brag-ai/commit/185f1b82f07d3926b0e562649e82383e349dc8b6))
- Add bash scripts for simplifying common tasks ([#14](https://github.com/ruancomelli/brag-ai/issues/14)) - ([017c57d](https://github.com/ruancomelli/brag-ai/commit/017c57db94b9b89a1bcea414f44076526c57ba7f))
- Use `nox` as CI task runner ([#13](https://github.com/ruancomelli/brag-ai/issues/13)) - ([4ae9a11](https://github.com/ruancomelli/brag-ai/commit/4ae9a11a6e4cb7305652244be045936d024cc6e3))
- Add CI ([#7](https://github.com/ruancomelli/brag-ai/issues/7)) - ([db52cfe](https://github.com/ruancomelli/brag-ai/commit/db52cfe0e0a0a545c61e5f475ce27b3bb9af9fda))

### 📦 Dependencies

- *(deps)* Update orhun/git-cliff-action action to v4 ([#34](https://github.com/ruancomelli/brag-ai/issues/34)) - ([fd9b75c](https://github.com/ruancomelli/brag-ai/commit/fd9b75c91774070678d90d433e21818aeafa640c))
- *(deps)* Update kenji-miyake/setup-git-cliff action to v2 ([#33](https://github.com/ruancomelli/brag-ai/issues/33)) - ([d000d07](https://github.com/ruancomelli/brag-ai/commit/d000d074f312af12276bf4316a6b80e9037f3094))

## New Contributors ❤️

* @GerdDowideit made their first contribution
* @ruancomelli made their first contribution in [#40](https://github.com/ruancomelli/brag-ai/pull/40)
* @renovate[bot] made their first contribution in [#34](https://github.com/ruancomelli/brag-ai/pull/34)<!-- generated by git-cliff -->
