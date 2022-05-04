# noAim-Translation

This is a small program to simplify the text translation process for the [Arma 3 noAim server](https://www.noaim.eu/)

The objective is to visualize in the same window the original text to be translated, and to have a text field for the translated text that we will fill (or modify the translation already done), the whole thing, automatically making the changes in the file.

## Application
<div align="center">
   <img src="https://user-images.githubusercontent.com/46728024/166704989-6ed694cb-d053-453d-91a9-95e9813eefc0.png" width="90%" height="90%">
</div>

## How to install and run

### Install from release (recommended)

- [Download the last release](https://github.com/Gyrfalc0n/noAim-Translation/releases/download/1.0/noAim.Translator.v1.0.exe)
- Put the file `stringtable.xml` (the file must be called exactly that) in the same directory as the executable you just downloaded
- You are free to run `noAim-Translator-v1.0.exe `.
- All changes are saved in the `stringtable_translated.xml` file in the same directory

### Install from source

- Clone this git repository : 
```bash
git clone https://github.com/Gyrfalc0n/noAim-Translation.git
```
- Install requirements : 
```bash
pip install -r requirements.txt
```
- Put the file `stringtable.xml` (the file must be called exactly that) in the same directory than the `translator.py` file
- Run the application : 
```bash
python3 translator.py
```

## How to use

1. Select languages to translate to
2. Check `Revision Mode` if you want to see text in the selected language that are already translated (useful to modify existing translation)
3. Check `Unscaped Mode` to see `xml` and `html` tag in a more human friendly way (checked by default)
4. Click `Confirm translation` to start
5. Navigate through text to translate with `Next text` and `Previous text`
6. Click `Reset text` to rest current text to its default value (value from file)
7. Translate text in the box (must match patern with original text (if there are some tags...))
8. Click `Confirm translation` to automaticaly write translation to output file and go to the next text to translate
9. Close app when done

## How it works 

1. Read informations from `stringtable.xml` and store them in memory
2. Sort them by languages, packages, and key
3. Display in the same window (Original text, already translated or blank (is no translation is made yet) and some options)
4. Write translation in the output file
5. Navigate through texts (key) to translate

## Limits

- It is still necessary to merge the different files translated in the different languages

## Upcoming features

- Merge files feature
- Application Icon
- More input control

------

`Author : Gyrfalcon`
`Discord : Gyrfalcon#1911`

