from moniv import Moniv

moniv = Moniv()
try:
    1 / 0
except Exception as e:
    moniv.capture_exception(e, context={"user": "saleh"})
