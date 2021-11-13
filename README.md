# bankapp

<div align="center">

[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/bankapp/bankapp/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/bankapp/bankapp/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/bankapp/bankapp/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

bankapp is a practice project in python to set up a bank model with entities such as customers and employees and services and methods.

</div>

## Installation


1. Clone the repository with git bash (or download from GitHub):

```bash
git clone https://github.com/shaizamzaheer/bankapp.git
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

- If you are using Windows, use <https://stackoverflow.com/questions/36770716/mingw64-make-build-error-bash-make-command-not-found> to get make.

<p>

3. Initialize poetry 

```bash
make install
```

4. Run the codestyle:

```bash
make codestyle
```

5.  Run help

```bash
poetry run bankapp --help
```

### Makefile usage

[`Makefile`](https://github.com/bankapp/bankapp/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies </summary>
<p>

Install requirements:

```bash
make install
```

</p>
</details>

<details>
<summary>3. Tests </summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/bankapp/bankapp/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

## 🛡 License

[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/bankapp/bankapp/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{bankapp,
  author = {bankapp},
  title = {bankapp is a practice project in python to set up a bank model with entities such as customers and employees and services and methods.},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/bankapp/bankapp}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
