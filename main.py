from pyscript import document, display

 

# Python dictionary: Symbol -> (Element Name, Atomic Number, Atomic Mass)
non_metals = {
    "H":  ("Hydrogen",   1,   1.008),
    "He": ("Helium",     2,   4.0026),
    "C":  ("Carbon",     6,   12.011),
    "N":  ("Nitrogen",   7,   14.007),
    "O":  ("Oxygen",     8,   15.999),
    "F":  ("Fluorine",   9,   18.998),
    "Ne": ("Neon",       10,  20.180),
    "P":  ("Phosphorus", 15,  30.974),
    "S":  ("Sulfur",     16,  32.06),
    "Cl": ("Chlorine",   17,  35.45),
    "Ar": ("Argon",      18,  39.948),
    "Se": ("Selenium",   34,  78.971),
    "Br": ("Bromine",    35,  79.904),
    "Kr": ("Krypton",    36,  83.798),
    "I":  ("Iodine",     53,  126.904),
    "Xe": ("Xenon",      54,  131.293),
    "Rn": ("Radon",      86,  222),
}

def check_details(event):
    # Element1 holds the value of the input whose id="Element1" in the HTML
    Element1 = document.getElementById("Element1").value.strip().capitalize()
    box = document.getElementById("result")
    box.innerHTML = ""

    if Element1 == "":
        box.className = "result-box not-found"
        box.textContent = "Please enter an element symbol."
        return

    result = non_metals.get(Element1, ("Element not found", "-", "-"))

    if result[0] == "Element not found":
        box.className = "result-box not-found"
        box.textContent = "The element '" + Element1 + "' does not exist in the non-metals list."
    else:
        box.className = "result-box found"
        box.innerHTML = (
            "<div><strong>Symbol:</strong> " + Element1 + "</div>"
            "<div><strong>Element:</strong> " + result[0] + "</div>"
            "<div><strong>Atomic Number:</strong> " + str(result[1]) + "</div>"
            "<div><strong>Atomic Mass:</strong> " + str(result[2]) + "</div>"
        )

# Python is ready: enable the button
btn = document.getElementById("checkBtn")
btn.disabled = False
btn.textContent = "Check Details"
  </script>

</body>
</html>
