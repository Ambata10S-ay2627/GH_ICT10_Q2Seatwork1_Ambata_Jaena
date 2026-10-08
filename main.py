# The Nickname Atlas

from pyscript import display, document

def reveal_name(e):
    nickname = document.getElementById("southeast_asia")
    southeast_asia = str(nickname).value

    display(f'The nickname of this Southeast Asian country is "{southeast_asia}"', target='output')
