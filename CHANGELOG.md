# Changelog

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

* @ruancomelli made their first contribution in [#40](https://github.com/ruancomelli/brag-ai/pull/40)
* @renovate[bot] made their first contribution in [#34](https://github.com/ruancomelli/brag-ai/pull/34)<!-- generated by git-cliff -->
