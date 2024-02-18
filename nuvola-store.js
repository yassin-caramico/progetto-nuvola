var formHtml = `
<p>Come possiamo aiutarti oggi?</p>
<form id="search-form">
    <input type="text" id="query" placeholder="Cosa stai cercando oggi?">
    <button type="submit">Cerca</button>
</form>
`;

document.getElementById("risultato-ricerca").innerHTML = formHtml;

document
  .getElementById("search-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Evita il comportamento predefinito del submit

    var inputQuery = document.getElementById("query").value;

    fetch("/cerca", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: inputQuery }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById(
          "risultato-ricerca"
        ).innerHTML = `<p>${data.result}</p>`;
      })
      .catch((error) => {
        console.error("Errore nella ricerca:", error);
      });
  });
