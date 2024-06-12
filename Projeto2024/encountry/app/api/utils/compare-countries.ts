import axios from "axios"
import { graphdbEndpoint } from "./endpoint"

export async function compareCountries(
  country1: string,
  country2: string,
  row: string,
) {
  const sparqlQuery = `
    PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
    SELECT ?valor1 ?valor2 WHERE {
      ?country2 :nome "${country2}".
      ?country1 :${row} ?valor1.
      ?country2 :${row} ?valor2.
      ?country1 :nome "${country1}".
    }
  `

  try {
    const response = await axios.get(graphdbEndpoint, {
      params: { query: sparqlQuery },
      headers: { Accept: "application/sparql-results+json" },
    })

    if (response.data.results.bindings.length === 0) {
      console.error("No data found for the given query.")
      return null
    }

    let v1 = response.data.results.bindings[0].valor1.value.replace(",", ".")
    let v2 = response.data.results.bindings[0].valor2.value.replace(",", ".")

    if (
      row === "hemisferio" ||
      row === "lado_em_que_conduz" ||
      row === "moeda" ||
      row === "continente"
    ) {
      return v1.toLowerCase() === v2.toLowerCase() ? "right" : "wrong"
    } else if (row === "longitude") {
      const longitude1 = parseFloat(v1)
      const longitude2 = parseFloat(v2)

      if (isNaN(longitude1) || isNaN(longitude2)) {
        console.error("Parsed values are not numbers:", {
          longitude1,
          longitude2,
        })
        return null
      }

      return longitude1 < longitude2
        ? "r"
        : longitude1 > longitude2
          ? "l"
          : "right"
    } else {
      v1 = parseFloat(v1.replace(/[$%]/g, ""))
      v2 = parseFloat(v2.replace(/[$%]/g, ""))
      if (isNaN(v1) || isNaN(v2)) {
        console.error("Parsed values are not numbers:", { v1, v2 })
        return null
      }
      return v1 < v2 ? "u" : v1 > v2 ? "d" : "right"
    }
  } catch (error: any) {
    console.error("Error making SPARQL query:", error.message)
    if (error.response) {
      console.error("Response data:", error.response.data)
      console.error("Response status:", error.response.status)
      console.error("Response headers:", error.response.headers)
    } else if (error.request) {
      console.error("No response received:", error.request)
    } else {
      console.error("Error message:", error.message)
    }
    return null
  }
}
