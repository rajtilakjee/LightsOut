# LightsOut
*Because even your PC needs rest.*

LightsOut is a simple app that shuts down your PC after a specific time set by the user.

![screenshot](/images/screenshot.png)

This is part of a contest held on [r/developersIndia](https://new.reddit.com/r/developersIndia/) organized by [ZnV1](https://www.reddit.com/user/ZnV1/).

The requirements were to create an app that takes a time (say 5 mins) and shuts the PC down once that time is up.

## Mandatory app features:
- Should take a time
- Should shut down after that time
- Final app should be easily shareable and runnable by a normal user (asking them to install is okay, asking them to compile etc is not)

## How to use
- Download the app
- Open the app
- Fill in the time (in minutes) after which you would like your PC to shutdown
- Click on the "+" button

## Roadmap
The following features will be added in due time:
- [ ] - Cancel shutdown
- [ ] - In-app Help and FAQ
- [ ] - Light and Dark themes
- [ ] - App minimization in System Tray
- [ ] - UI enhancements

## Installation
To install LightsOut for local development execute the following steps:
- Clone the repo: `git clone https://github.com/rajtilakjee/lightsout`
- Create virtual environment: `python -m venv .venv`
- Activate virtual environment: `.venv\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`
- Run LightsOut: `flet run`

## Built with
- Flet

## Contributing
Contributions are welcome! Fork the repository and submit a pull request with your enhancements or bug fixes. See the [CONTRIBUTING](CONTRIBUTING.md)file for more details.

## License
This project is licensed under the MIT license - see the [LICENSE](LICENCE) file for more details.