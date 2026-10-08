# The Nickname Atlas

from pyscript import display, document

def reveal_name(e):
    nickname = document.getElementById("sea")
    sea = nickname.value

    display(f'The nickname of this Southeast Asian country is "{sea}"', target='present', append=False)
