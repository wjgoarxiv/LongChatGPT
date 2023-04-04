# LongChatGPT
::An effective tool to input long contents to ChatGPT::

<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/release/python-370/)

*LongChatGPT is a tool for inputting long contents to [ChatGPT](https://chat.openai.com/). Note that this repository is extended repository of [PaperSumGPT](https://github.com/wjgoarxiv/PaperSumGPT). If you want to perform a same task as PaperSumGPT, use the `initial prompt` entitled `Abbreviator`, and `final prompt` entitled `Paper-abbreviation`.*

> *(What are __initial & final prompts__? See [(2) Run `longchatgpt` to toss long contents to ChatGPT](#2-run-longchatgpt-to-toss-long-contents-to-chatgpt))*

## Table of Contents
- [CAUTION: For ChatGPT free users!](#caution-for-chatgpt-free-users)
- [How to Install](#how-to-install)
  - [(0) For Windows users (first time only!)](#0-for-windows-users-first-time-only)
  - [(1) Clone this repository](#1-clone-this-repository)
  - [(2) Install dependencies](#2-install-dependencies)
  - [(3) Install LongChatGPT](#3-install-longchatgpt)
- [Usage](#usage)
  - [(1) Run `chatgpt_wrapper` before using `longchatgpt`](#1-run-chatgpt_wrapper-before-using-longchatgpt)
  - [(2) Run `longchatgpt` to toss long contents to ChatGPT](#2-run-longchatgpt-to-toss-long-contents-to-chatgpt)
- [Contributing](#contributing)

- [Dependencies](#dependencies)
- [License](#license)

## CAUTION: For ChatGPT free users!
> [2023-04-04 updated]

After I tested with several accounts with ChatGPT, I found that there were __significant differences in the performance of ChatGPT__ depending whether the account is a free user or a paid user (*ChatGPT Plus*).

If you are a free user of ChatGPT, and you have a long paper to summarize, I recommend you to (1) upgrade your account to __[ChatGPT Plus](https://openai.com/blog/chatgpt-plus)__, or (2) repeat the input process several times to get better results.

Unfortunately, the free version of ChatGPT cannot understand and store the long context of the input text, which leads to a poor performance.

## How to Install

> If you are using Mac, you can skip [(0) For Windows users](#0-for-windows-users) step.

> ### (0) For Windows users (first time only!)
> Since there are no pre-built binaries for Windows, follow the instructions below to install LongChatGPT on Windows.
> 1. In the search tab, type `Turn Windows features On (Windows 기능 켜기/끄기 in Korean)`. Then, check the box of `Windows Subsystem for Linux`. 
> 2. Next, reboot your computer.
> 3. Now, you need to install [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW?hl=en-us&gl=kr&rtc=1) in your local computer.
> 4. Open Ubuntu and make your UNIX accounts and passwords.
> 5. For ease of use, you should install `Anaconda` by following commands (copy and paste them in your terminal, one by one)
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

### (2) Run `longchatgpt` to toss long contents to ChatGPT
After running `chatgpt_wrapper`, you can use `longchatgpt` to toss long contents to ChatGPT. You can use `longchatgpt` by typing the following command: 
  
  ```bash
  longchatgpt
  ```

The following message would be shown: 

```text
INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. PDF (`.pdf`) file
    3. Text (`.txt`) file

    Note that the option 2 would convert the PDF file to a markdown file using the `PyPDF2` package:
```
Depending on your file type, you can choose the corresponding option. For demonstration, I'll use the following article published in [Healthline](https://www.healthline.com/nutrition/best-ways-to-get-abs). I just manually downloaded the web article into PDF file. Please refer to the `demoinput.pdf` file in the repository that I uploaded. Check your cloned repository to see the file. (~~Note that this article is about how to get **abs** 😂~~)

Since we have to input PDF file, we can type `2` and press `Enter` key. 

```text
------------------------------------------------
+---------------+-----------------+
|   File number |    File name    |
|---------------+-----------------|
|             1 | ./demoinput.pdf |
+---------------+-----------------+
------------------------------------------------

INFO: Please select the file number or press "0" to exit:
```
I typed `1` and pressed `Enter` key. 

```text
------------------------------------------------
INFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n):
```
I do NOT want to turn on `verbose` mode, so I typed `n` and pressed `Enter` key. 

```text
INFO: Please type the number the ChatGPT model that you want to use:

    1. default (Turbo version for ChatGPT Plus users and default version for free users)
    2. gpt4 (Only available for ChatGPT Plus users; a little bit slower than the default model)
    3. legacy (Only available for ChatGPT Plus users; an older version of the default model)

    Note that the option 2 and 3 are NOT available for free users. If you are the free user, please select the option 1

    :
```
I typed `1` and pressed `Enter` key. 
Since the input file was PDF, the program will convert the PDF file to a markdown file using the `PyPDF2` package. The following message would be shown: 

```text
------------------------------------------------
INFO: Converting the PDF file to a markdown file...
INFO: The PDF file has been converted to a markdown file.
------------------------------------------------
```

From now on, we have to **focus on** the following procedures:

```text
----------------------------------------
INFO: Let's select the initial prompt. Choose a method to select the initial prompt.

1. Add custom initial prompt
2. Select initial prompt
3. Delete initial prompt
4. Write initial prompt here
5. Exit
Enter your choice:
```
As terminal asks, we can choose the way to input the *initial prompt* to ChatGPT. As the writer of [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts) mentioned, giving the role to ChatGPT is a good way to get the desired outputs. One of the best ways to hack ChatGPT is using the magical keyword `act as...`. For instance, if I want to get the desired outputs related to the nutrition, I can make an initial prompt like `Please, act as a nutritionist...`. The `longchatgpt` can manage these initial prompts as JSON format. If this is the first time to run `longchatgpt`, the program will create a JSON file named `initial_prompts.json` in the current directory. Newly formed JSON file looks like the following: 

```json
{
    "Role 1": "Initial prompt 1",
    "Role 2": "Initial prompt 2",
    "Role 3": "Initial prompt 3",
}
```
Therefore, it is easy to manage your own prompt library. Add your own initial prompts to the JSON file and use them whenever you want. If you have any ideas to share your initial prompts, please feel free to make a **pull request** to this repository. I'll be happy to receive your contributions. 

I'll use the template initial prompt saved in `initial_prompts.json` as an example. First, let's `Enter your choice:` and type `2` and press `Enter` key. 

```text
INFO: Available roles:
- Abbreviator
- Essay-writer
- JailbreakGPT
- Journal-reviewer
- Machine-learning-engineer
- MailGPT
- Pro-journalist
- Proof-reader
- Python-copilot
- Report-writer

INFO: Enter the role you want to use:
```
I typed `Journal-reviewer` and pressed `Enter` key. 
The `Journal-reviewer` initial prompt is as follows: 

```json
{
  "Journal-reviewer": "As a journal author, I require you to review and critique my article submitted for publication. You will critically evaluate my research, approach, methodologies, and conclusions, and offer constructive criticism on their strengths and weaknesses. Please provide me with the guidelines or criteria for the review process, such as the expected word count or submission deadlines. As part of your role as a journal reviewer, you will conduct a thorough and rigorous evaluation of my article, assessing its research methodology, data analysis, and overall contribution to the field. You will also provide clear and constructive feedback on the article's strengths and weaknesses, and suggest specific areas for improvement or further development. Furthermore, I understand the importance of maintaining confidentiality and anonymity in the peer review process. You will ensure that my article is reviewed in a timely and professional manner, while maintaining strict confidentiality and adhering to the ethical standards of the journal. I'll now have to provide you with the article to review. The important thing is that you should NOT answer directly or respond to the previous message. Make sure that you have to accomplish the task when all the inputs are given. I'll let you know if all the inputs are given. Thank you.",
}
```

Now, initial prompt is tossed to ChatGPT. The following message would be shown: 

```text
INFO: Tossing initial prompt...
INFO: ChatGPT started consuming all the input contents...
INFO: Waiting for ChatGPT to respond for 1/2 part(s)...
INFO: 1/2 part(s) tossed to ChatGPT.
INFO: Waiting for ChatGPT to respond for 2/2 part(s)...
INFO: 2/2 part(s) tossed to ChatGPT.
```

After the iteration, the program will ask you to input the `final prompt`. 
```text
----------------------------------------
INFO: Next, let's select the final prompt. Choose a method to select the final prompt.

1. Add custom final prompt
2. Select final prompt
3. Delete final prompt
4. Write final prompt here
5. Exit
Enter your choice:
```
You can also manage your own final prompt library. The `longchatgpt` will create a JSON file named `final_prompts.json` in the current directory. Newly formed JSON file looks like the following: 

```json
{
    "Prompt 1": "Final prompt 1",
    "Prompt 2": "Final prompt 2",
    "Prompt 3": "Final prompt 3",
}
```

In the same manner, I'll use the template final prompt saved in `final_prompts.json` as an example. First, let's `Enter your choice:` and type `2` and press `Enter` key. 

```text
INFO: Available final prompts:
- Paper-abbreviation
- code-revision
- JAILBREAK
- Review
- Journalism
- Education
```
I typed `Review` and pressed `Enter` key.

```text
INFO: Selected final prompt: Now, all the inputs are given to you. You should write your complete review by fitting into the following format. The format is as follows:

------ TEMPLATE STARTS ------

# **[TITLE]**
## Review
[REVIEW]

------ TEMPLATE ENDS ------

And please, write the outputs thinking you are writing PPT slides. But NOT too simple. You have to write the outputs in a way that the readers can understand the contents easily. Do NOT consider the output length limit!
```

After a few second, the program will show the output file to user.
```text
INFO: Response from ChatGPT: # **The Best Ways to Get Abs (With or Without a Six-Pack)**

## Review

This article provides a comprehensive overview of six-pack abs, including what they are, the factors that affect abdominal development, and strategies for building a strong, functional core. The article emphasizes that while having visible abs may be an aesthetically appealing goal for many, the primary benefits of core training go far beyond appearances.

The article discusses the rectus abdominis muscle, which is responsible for flexing the spine forward and is commonly associated with visible six-pack abs. However, the article emphasizes that the rectus abdominis is just one of many muscles in the core, and that core training should target all of these muscles for optimal benefits.

The article also discusses the role of body fat percentage in determining the visibility of six-pack abs, emphasizing that a low body fat percentage is necessary to reveal a chiseled six-pack. The article provides a range of typical ballpark body fat percentages for men and women that are associated with visible six-pack abs, and notes that genetics, lifestyle factors, and calorie intake can all affect where an individual tends to store and burn fat.

The article provides practical tips for building a strong, functional core, including exercises that occur in all planes of motion and static and movement-based exercises to train both stability and motion in the core muscles. The article also provides lifestyle strategies for reducing body fat percentage, including getting adequate sleep, exercising regularly with weights and cardio, eating a healthy diet high in fresh fruits, vegetables, and lean proteins, and choosing water over sugary drinks.

Overall, this article provides a well-rounded overview of six-pack abs and core training, emphasizing the importance of building a strong, functional core for improved health and well-being, rather than focusing solely on appearance. The article provides practical tips and strategies for achieving a visible six-pack, while also emphasizing the challenges of maintaining a low body fat percentage and the importance of maintaining a healthy lifestyle for long-term health benefits.

INFO: Does the answer seem to be truncated? (y/n):
```
Note that the program finally asks you whether the answer seems to be __truncated or not__. When you treat a large input file, the program sometimes truncates the answer (maybe this is due to the limitation of the web-based engine). If you think the answer is truncated, you can try to continue the output exportation by typing `y` and pressing `Enter` key. Then, the program will concatenate all the intermediate outputs (but don't trust this functionality too much, since the outputs from ChatGPT are NOT always exact, and sometimes ChatGPT will show an unexpected output). 

In this example, I typed `n` because it seems that the answer is not truncated. 

```text
INFO: Choose output format (stream / txt / md):
```
The `longchatgpt` program will ask you to choose the output format. You can choose `stream`, `txt` (text format), or `md` (markdown format). In this example, I chose `md` and pressed `Enter` key. 

```text
INFO: Output saved as OUTPUT.md
```
Now, the program will save the output file as `OUTPUT.md` in the current directory. You can check the `demoOUTPUT.md` file in the `demo` directory. 

Note that ChatGPT sometimes makes undesired outputs. In this case, you should try a few times to get the best result. You can revise prompts or intermediate chat contents, you can visit [ChatGPT official website](https://chat.openai.com). Good luck with your works! 💪🏻

## Contributing 
To enhance the `longchatgpt` program, please share your initial & final prompt ideas, and your feedbacks. Use `Pull Requests` to contribute to the project. The power of collective intelligence would be the best way to improve the program! 🔌

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading and processing PDF files.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/longchatgpt).
