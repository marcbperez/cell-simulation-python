# cell-simulation-python

A simulation environment written in Python and OpenGL. Supports element
behavior, interaction and a simple physics environment.

## Installation

This project uses Gradle (at least version 3.3) as its build system. On Ubuntu
Linux distributions Gradle can be installed with the following commmands:

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:cwchien/gradle
sudo apt-get update
sudo apt-get install default-jdk gradle=3.4-0ubuntu1
```

Project and system dependencies are managed by the build script. To install them
get the latest version and run the `dependencies` task:

```bash
git clone https://github.com/marcbperez/cell-simulation-python
cd cell-simulation-python
sudo -H gradle dependencies
```

## Usage

This project can be installed with pip and used as a Python package.

```python
from cellsimulation.scene import Scene
```

## Testing

Tests will be executed by default every time the project is built. A coverage
report will be generated under `htmlcov/index.html`. To get a complete list of
build tasks, check `tasks`:

```bash
sudo -H gradle
sudo -H gradle test
sudo -H gradle tasks --all
```

## Troubleshooting

The [issue tracker][issue-tracker] intends to manage and compile bugs,
enhancements, proposals and tasks. Reading through its material or reporting to
its contributors via the platform is strongly recommended.

## Contributing

This project adheres to [Semantic Versioning][semver] and to certain syntax
conventions defined in [.editorconfig][editorconfig]. To get a list of changes
refer to the [CHANGELOG][changelog]. Only branches prefixed by *feature-*,
*hotfix-*, or *release-* will be considered:

  - Fork the project.
  - Create your new branch: `git checkout -b feature-my-feature develop`
  - Commit your changes: `git commit -am 'Added my new feature.'`
  - Push the branch: `git push origin feature-my-feature`
  - Submit a pull request.

## Credits

This project is created by [marcbperez][author] and maintained by its
[author][author] and contributors.

## License

This project is licensed under the [Apache License Version 2.0][license].

[author]: https://marcbperez.github.io
[issue-tracker]: https://github.com/marcbperez/cell-simulation-python/issues
[editorconfig]: .editorconfig
[changelog]: CHANGELOG.md
[license]: LICENSE
[semver]: http://semver.org
[install-docker-compose]: https://docs.docker.com/compose/install/
