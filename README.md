# LongChatGPT
::An effective tool to input long contents to ChatGPT::

<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/release/python-380/)

*LongChatGPT is a tool for inputting long contents to [ChatGPT](https://chat.openai.com/).* 

## Table of Contents
- [CAUTION: For ChatGPT free users!](#caution-for-chatgpt-free-users)
- [How to Install](#how-to-install)
  - [(0) For Windows users (first time only!)](#0-for-windows-users-first-time-only)
  - [(1) Clone this repository](#1-clone-this-repository)
  - [(2) Install dependencies](#2-install-dependencies)
  - [(3) Install LongChatGPT](#3-install-longchatgpt)
- [Usage](#usage)
  - [(1) Run `chatgpt_wrapper` before using `longchatgpt`](#1-run-chatgpt_wrapper-before-using-longchatgpt)
  - [(2) Run `longchatgpt` to summarize the content of a paper](#2-run-longchatgpt-to-summarize-the-content-of-a-paper)
- [Dependencies](#dependencies)
- [License](#license

## CAUTION: For ChatGPT free users!
> [2023-04-04 updated]

After I tested with several accounts with ChatGPT, I found that there were __significant differences in the performance of ChatGPT__ depending whether the account is a free user or a paid user (*ChatGPT Plus*).

If you are a free user of ChatGPT, and you have a long paper to summarize, I recommend you to (1) upgrade your account to __[ChatGPT Plus](https://openai.com/blog/chatgpt-plus)__, or (2) repeat the input process several times to get better results.

Unfortunately, the free version of ChatGPT cannot understand and store the long context of the input text, which leads to a poor performance.

## How to Install

> If you are using Mac, you can skip [(0) For Windows users](#0-for-windows-users) step.

> ### (0) For Windows users (first time only!)
> Since there are no pre-built binaries for Windows, follow the instructions below to install PaperSumGPT on Windows.
> 1. In the search tab, type `Turn Windows features On (Windows 기능 켜기/끄기 in Korean)`. Then, check the box of `Windows Subsystem for Linux`. 
> 2. Next, reboot your computer.
> 3. Now, you need to install [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW?hl=en-us&gl=kr&rtc=1) in your local computer.
> 4. Open Ubuntu and make your UNIX accounts and passwords.
> 5. For ease of use, you should install `Anaconda` by following instructions. 
>     ```
>     wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
>     ```
>     ```
>     bash Anaconda3-2019.10-Linux-x86_64.sh
>     ```
>     Read all the instructions with Enter and type `yes` to agree with the license.
> 
>     ```
>     source ~/.bashrc
>     ```
> 
>     Now, type
>     ```
>     conda activate
>     ```
>     in your terminal. If you see `(base)` in your terminal, you have successfully installed Anaconda.
> 6. Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/) in your local computer.
>     Download `VcXsrv` installer and run it. <br/>
>     Then, click `Finish`. 
>     
>     Next, open `XLaunch` and click `Next`.
> 
>     After you open `XLaunch`, you should check the following options:
>     - [x] Multiple windows
>     - [x] Start no client
>     - [x] Disable access control
> 
>     Done! Now let's move on to the terminal.
> 
> 7. Type the below commands in your terminal. 
>     ```
>     sudo systemd-machine-id-setup
>     ```
>     ```
>     sudo dbus-uuidgen --ensure
>     ```
>     ```
>     cat /etc/machine-id
>     ```
>     If terminal shows a long string of numbers and letters, you have successfully installed `systemd-machine-id-setup` and `dbus-uuidgen`.
> 
>     Finally, you can install `x11-apps` by typing the following command:
>     ```
>     sudo apt-get install x11-apps xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic
>     ```
> 
>     Add the environment variable `DISPLAY` to your `.bashrc` file by typing the following command:
>     ```
>     echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
>     sudo /etc/init.d/dbus start &> /dev/null" >> ~/.bashrc
>     ```
>     ```
>     source ~/.bashrc
>     ```
> 
>     Test your X11 GUI by typing the following command:
>     ```
>     xeyes
>     ```
>     If you see a pair of eyes, you have successfully installed X11 GUI.
> 
> These steps are essential (in Windows) for successfully executing `playwright` in Windows terminal (which is critical when you configure your `ChatGPT` account).

### (1) Clone this repository
You can install LongChatGPT by cloning this repository and install it from the source:

```bash
git clone https://github.com/wjgoarxiv/LongChatGPT.git
```
```bash
cd LongChatGPT/
```

### (2) Install dependencies
And you must use `install_old-repo.sh` to install the legacy version of `chatgpt_wrapper`. The new version of `chatgpt_wrapper` is not compatible with the current version of `longchatgpt` (since the new version of `chatgpt_wrapper` will use the ChatGPT API, not the stream-based one).
```bash
chmod +x * 
```
```bash
./install_old-repo.sh
```

### (3) Install LongChatGPT
Then, you can install LongChatGPT by running the following command:

```bash
pip install .
```

## Usage
### (1) Run `chatgpt_wrapper` before using `longchatgpt`
Before using `longchatgpt`, you must run `chatgpt_wrapper` to start the ChatGPT server. 

Since you are first running `chatgpt_wrapper` in your computer, you might input the following command to install `playwright`:
```
playwright install
```
The *nightly* will be downloaded and installed in your local machine.

Next, you can use the following command to start the server:

```bash
chatgpt install
```
Login to your ChatGPT account in *Nightly* browser. If you see the chat window, close the browser and type `/exit` to close the `chatgpt_wrapper`. After that, you can restart the `chatgpt_wrapper` by running the following command:

```bash
chatgpt
```
This is the original functionality of `chatgpt_wrapper`. For more information, please visit the [chatgpt_wrapper github repository](https://github.com/mmabrouk/chatgpt-wrapper). 



----
Note that ChatGPT sometimes makes undesired outputs. In this case, you should try a few times to get the best result. Good luck with your works! 🚀

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading and processing PDF files.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/papersumgpt).
