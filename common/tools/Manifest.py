# success/core/creed.py

from random import choice

def print_success_creed():
    """Imprime el manifiesto sagrado del framework Success en el arranque."""

    creed = [
        "Success is better than failure.",
        "Errors are part of the contract.",
        "Clarity beats flexibility.",
        "If you break it, you bought it.",
        "Outside this framework your failure is success-ful.",
        "Aunque sea un failure, siempre será un Success.",
        "Te doy flexibilidad, pero tú no te gobiernas solo.",
        "Si te sales del contrato, prepárate pa’ reventar.",
        "Dentro del marco hay orden. Fuera, solo caos.",
        "No hay magia, solo contrato.",
        "Or run, or climb. Success te avisó.",
        "Success no se rompe, se expone.",
    ]

    border = "═" * 60
    print("\n" + border)
    print("             🧱 SUCCESS FRAMEWORK MANIFIESTO 🧱")
    print(border)
    for line in creed:
        print(f" • {line}")
    print(border + "\n")

def ascii_warning():
    print("""
=========================
=========================
   TE LO DIJE, POR AHÍ NO!
=========================
=========================
""")


def ascii_warning1():
    print("""
┌────────────────────────────┐
│  SUCCESS FRAMEWORK v2.0    │
│   Build apps. With soul.   │
└────────────────────────────┘
""")


def ascii_warning2():
    print("""
┌───────────────────────────────────────────┐
│        ✅ SUCCESSFUL RESPONSE             │
├───────────────────────────────────────────┤
│  status  : success                        │
│  message : Datos obtenidos correctamente │
│  data    : {...}                         │
└───────────────────────────────────────────┘
""")


def ascii_warning1():
    print("""
┌──────────────────────────┐
│   ❌ ERROR: VALIDATION   │
├──────────────────────────┤
│  message : Campo 'email' inválido │
└──────────────────────────┘
""")


