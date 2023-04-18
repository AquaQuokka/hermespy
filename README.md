# IMPORTANT {#important}

*HermesPy* is **ONLY** compatible with ***Windows***.

*Notepad* **MUST** be installed for *HermesPy* to work.

# HermesPy

HermesPy is an SMTP client which is lightweight, fast, and easy to use.

# FAQ {#faq}

### Q: Why is HermesPy only compatible with Windows? {#windows}
#### A: HermesPy relies on the WinDLL framework to create dialogues, and HermesPy also depends on Notepad for editing messages. This will change eventually in future versions of HermesPy for compatibility with other operating systems. However, this will require integrating a text editor like [Newt](https://github.com/TheNewtProject/app) into the client. {#windows-a}


### Q: Why doesn't HermesPy work with attachments? {#no-files}
#### A: HermesPy currently only supports SMTP for sending emails, and SMTP does not support attachments so HermesPy cannot send attachments. {#no-files-a}


### Q: Why does HermesPy send emails but not receive them? {#no-inbox}
#### A: HermesPy is a Python script that only runs when you run the script, which means that in order to receive emails, the script would have to run 24/7. Also, it would have to download each email for reading, which is dangerous because the email could contain lots of text and could crash the computer, or it could contain harmful content or scripts. Also, if you receive lots of emails, it would fill up storage very quickly. {#no-inbox-a}


### Q: Why can't I log into my email? {#no-login}
#### A: If you are using Gmail, then you need to enable "Less secure apps" in your settings. For Outlook users, you need to generate an app password in your Microsoft account's security dashboard, and paste it into your `config.ini` file. However, if you are using the `config.ini` file for password storage or authentication, then you need to make sure that you do not accidentally (or deliberately) upload your `config.ini` file to the internet. This will allow people to log into your account without having to use multi-factor authentication. {#no-login-a}

### Q: Am I allowed to make a fork/mod of this repo? {#fork}
#### A: Of course! If you wish to make a fork of this repository, go ahead! As long as you don't blatantly steal any code, and make sure to credit me. If you wish to make a modded version of the application, then it must not contain any malicious code or offensive content. {#fork-a}


### Q: How can I contribute to this repository? {#contributing}
#### A: Fork the repository and submit a pull request. This will allow developers of HermesPy to review code changes and features, and if they are accepted, then they will automatically "merge", "squash", or "rebase" with the latest version of the original repository. {#contributing-a}


### Q: Is HermesPy safe to use? {#safe}
#### A: HermesPy does not contain any malicious code or offensive content, but sometimes security vulnerabilities may slip through. If you use this application, you do so at your own risk. {#safe-a}


### Q: My question isn't here, what should I do? {#no-faq}
#### A: If you are unsure about anything, open an issue on GitHub and ask me! If you wish to add a question to the FAQ, then please submit a pull request. {#no-faq}



# Instructions {#instructions}

1. Download the repository as `.zip`
2. Extract the archive.
3. Edit the `config.ini` file as shown in `Figure 1`

```
[config]
host = smtp.example.com
port = 587
you = john.smith@example.com
password = *
```
##### *Figure 1* {#figure-1}



#### What is my SMTP host address? {#host}

Here are some of the common ones:

Gmail: `smtp.gmail.com`<br/>
Outlook/Hotmail: `smtp.office365.com`<br/>
Courvix: `box.courvix.com`


If you want to not have to enter your password every time, change `*` to your password.

If you use multi-factor authentication, you will need to generate an app password.

#### How to generate an app password. (Microsoft) {#app-pwd}

1. Go to https://account.microsoft.com/security/
2. Click "Advanced security options"
3. Scroll down until you see "App passwords"
4. Press "Create a new app password"
5. Copy the generated password and paste it into `config.ini`


## Sending an Email {#send}

1. Run the Python file via `py main.py`
2. Enter the recipient's email.
3. Enter the subject.

A file called `message.txt` will open in Notepad.

4. Enter your email body in the file.
5. Press `Ctrl+S`

A file dialogue will open.

6. Press `Save`

A dialogue will open asking you if you wish to overwrite `message.txt`

7. Press `Yes`
8. Move back to `message.txt`
9. Close Notepad.
10. Press `OK` in the `WinDLL` dialogue that appears.

## Saving a Draft {#draft-1}

1. Follow steps `1-9` of `Sending an Email`, and press `Cancel` in the `WinDLL` dialogue that appears.

## Sending a Draft {#draft-2}

1. Open your folder where your installation of *HermesPy* is located.
2. If a folder called `drafts` does not exist, run `draft.py`
3. In the folder called `drafts` find the draft that you wish to send.
4. Instead of running `main.py`, run `draft.py`
5. It will ask you who you wish to send the email to. Enter the email as you would normally.
6. It will then ask you for a "draft ID".
7. Get the ID of the draft.
8. Enter the ID.
9. The email will be sent.


## Sending a Prefab {#prefab}

1. Open your folder where your installation of *HermesPy* is located.
2. If a folder called `prefabs` does not exist, run `prefab.py`
3. In the folder called `prefabs` create another folder. You can name this folder whatever you like.
4. Inside the subfolder, create a file called `template.json`
5. Open your `template.json` file in Notepad or your favourite text editor.
6. Format the file like so:
```
{"subject": "Your subject here", "body": "Your email body here"}
```
7. Save and Exit.
8. Instead of running `main.py`, run `prefab.py`
9. It will ask you who you wish to send the email to. Enter the email as you would normally.
10. It will then ask you for a "prefab ID".
11. Find the name of your folder in which your `template.json` file is located.
12. Enter the name of the folder in the prompt.
13. The email will be sent.

## Formatting a Prefab Message {#format}

1. Create a new file in your prefab folder called `varfile`.
2. Add some tags to your prefab in `template.json` like so:

```
{"subject": "Regarding <regard>", "body": "I need to contact you about <regard_concerns>."}
```

3. For each tag in your prefab, create a new line and tag declaration like so:

```
<regard>
<regard_concerns>
```

4. Save your `varfile` and `template.json` files.

If you do not require any tags in your prefab, then you can skip creating a `varfile` file and/or declarations.
