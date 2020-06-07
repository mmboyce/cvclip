# CVClip

This is a command line utility to help with the process of submitting cover letters.
All you have to do is supply the company title and the title of the position and it will print the modifications to
the console.

## Setup

Simply use the provided `cover.txt` file to write your cover letter. Whenever you feel inclined to type the name of the
company you're applying to, type `$CT`. Likewise, for the title of the position type `$PT`.

Any line beginning with `#` will be ignored.

## Use

`python cvclip -c "Microsoft" -p "Software Engineer"`

### Required Parameters

- `-c "COMAPNY_TITLE_HERE"` or `--company="COMPANY_TITLE_HERE"`
    - This is the title of the company you are applying to. This will replace occurrences of `$CT` in `cover.txt`
- `-p "POSITION_TITLE_HERE"` or `--position="POSITION_TITLE_HERE"`
    - This is the title of the position you are applying to. This will replace occurrences of `$PT` in `cover.txt`
    
### Optional Flags

- `-b` or `--clipboard`
    - This flag means that the resultant cover letter will be put into your clipboard for easy pasting.
        - **This will prevent printing to the console unless specified with the `-v` flag.**
- `-v` or `--verbose`
    - This flag will print the cover letter to the console. **This is presumed by default UNLESS you are using `-v` or 
    `-n`**
- `-n` or `--new`
    - This will create a new text file based on your template `cover.txt`. The new file will follow this naming
    convention: `$CT_$PT`
        - **Example usage:** `python cvclip -n -c "Github" -p "Markdown Expert"` would create a file named
        `Github_Markdown_Expert`
        - **This will prevent printing to the console unless specified with the `-v` flag.**
