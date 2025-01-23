from django.shortcuts import render
from django.http import JsonResponse


# Respuestas correctas
correct_answers = {
    "ficciones": {
        "page": 14,  # Página en su edición específica
        "next_clue": "Busca entre las historias de un joven rebelde cuyo lenguaje es único.",
    },
    "la naranja mecánica": {
        "page": 45,
        "next_clue": "Explora las historias donde el arte y la perfección se encuentran en un círculo.",
    },
    "decameron": {
        "page": 22,
        "next_clue": "Piensa en un detective atrapado en un cristal que distorsiona la realidad.",
    },
}

def check_answer(request):
    if request.method == "POST":
        book = request.POST.get("book", "").lower().strip()
        page = request.POST.get("page")

        # Validación de entradas
        if not book or not page or not page.isdigit():
            return render(request, "check.html", {
                "error": "Por favor, ingresa tanto el nombre del libro como un número de página válido."
            })

        # Verificar si el libro y la página coinciden
        page = int(page)
        if book in correct_answers and correct_answers[book]["page"] == page:
            return render(request, "check.html", {
                "success": "¡Correcto!",
                "next_clue": correct_answers[book]["next_clue"]
            })

        # Si es incorrecto
        return render(request, "check.html", {
            "error": "No es correcto. Intenta de nuevo."
        })

    return render(request, "check.html")