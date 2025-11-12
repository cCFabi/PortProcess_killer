<!-- Improved compatibility of back to top link -->

<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/cCFabi/PortProcess_killer">  
  <img width="80" height="80" alt="ChatGPT Logo" src="https://github.com/user-attachments/assets/7b01b8ab-9b02-4b0d-80a2-21a08f053ee4" />
  </a>

  <h3 align="center">Port Killer</h3>

  <p align="center">
    A simple Python GUI tool to find and kill processes running on specific ports.
    <br />
    <a href="https://github.com/cCFabi/PortProcess_killer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/cCFabi/PortProcess_killer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/cCFabi/PortProcess_killer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

---

## 📖 About The Project

Port Killer is a small but powerful utility that helps you identify and terminate any process that is listening on a specified port. It's written in Python using `PySimpleGUI` for the interface and `psutil` for process management.

### Features

* 🧠 Detects which process is listening on a given port
* 💀 Kills the process using Windows `taskkill`
* 💻 Simple, minimalistic GUI
* ⚙️ Lightweight and fast

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧰 Built With

* [Python 3](https://www.python.org/)
* [PySimpleGUI](https://pysimplegui.readthedocs.io/)
* [psutil](https://pypi.org/project/psutil/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 and pip installed. Then install dependencies:

```bash
pip install psutil PySimpleGUI
```

### Installation

1. Clone the repo

   ```bash
   git clone https://github.com/cCFabi/PortProcess_killer.git
   cd PortProcess_killer
   ```
2. Run the script

   ```bash
   python port_killer.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 💡 Usage

1. Enter the port number you want to free.
2. Click **Kill**.
3. The app will show the PID and terminate the process.

Example:

```bash
Port: 8080
```

Output:

```
Process running on port 8080 has PID: 1234
PID 1234 on Port 8080 has been killed
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🗺️ Roadmap

* [x] Basic GUI
* [x] Kill processes by port
* [ ] Cross-platform support (Linux/macOS)
* [ ] Show multiple results if several processes listen on the same port
* [ ] Add confirmation dialog before killing
* [ ] Add logging to file

See the [open issues](https://github.com/cCFabi/PortProcess_killer/issues) for a full list of proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/cCFabi/PortProcess_killer.svg?style=for-the-badge
[contributors-url]: https://github.com/cCFabi/PortProcess_killer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cCFabi/PortProcess_killer.svg?style=for-the-badge
[forks-url]: https://github.com/cCFabi/PortProcess_killer/network/members
[stars-shield]: https://img.shields.io/github/stars/cCFabi/PortProcess_killer.svg?style=for-the-badge
[stars-url]: https://github.com/cCFabi/PortProcess_killer/stargazers
[issues-shield]: https://img.shields.io/github/issues/cCFabi/PortProcess_killer.svg?style=for-the-badge
[issues-url]: https://github.com/cCFabi/PortProcess_killer/issues
[license-shield]: https://img.shields.io/github/license/cCFabi/PortProcess_killer.svg?style=for-the-badge
[license-url]: https://github.com/cCFabi/PortProcess_killer/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
