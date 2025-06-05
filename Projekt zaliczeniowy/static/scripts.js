document.addEventListener("DOMContentLoaded", function () {
    console.log("Strona załadowana!");

    // Obsługa formularza dodawania podróży
    const tripForm = document.querySelector("form");
    if (tripForm) {
        tripForm.addEventListener("submit", function (event) {
            const destination = document.getElementById("destination").value;
            const date = document.getElementById("date").value;

            if (!destination || !date) {
                alert("Proszę wypełnić wszystkie pola!");
                event.preventDefault();
            }
        });
    }

    // Obsługa usuwania rezerwacji
    const deleteButtons = document.querySelectorAll("form[action*='delete_reservation']");
    deleteButtons.forEach(button => {
        button.addEventListener("submit", function (event) {
            if (!confirm("Czy na pewno chcesz usunąć tę rezerwację?")) {
                event.preventDefault();
            }
        });
    });
});
