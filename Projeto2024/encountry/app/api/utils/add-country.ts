import axios, { AxiosResponse } from "axios"
import { graphdbEndpoint } from "./endpoint"
import { CountryDataEdit } from "@/lib/utils"

export async function addCountry(
  country: CountryDataEdit,
): Promise<AxiosResponse | null> {
  try {
    // Prepare countryString for SPARQL
    let countryString = ""
    for (const [key, value] of Object.entries(country)) {
      if (value) {
        // Ensure value is not empty
        countryString += `:${key} "${value}" ;\n`
      }
    }
    countryString = countryString.slice(0, -2) + " ."

    // Ensure country name is a string
    const nome =
      typeof country.nome === "string" ? country.nome : country.nome[0]

    // Prepare SPARQL query
    const sparqlQuery = `
      PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
      INSERT DATA {
        :${nome.replace(/\s+/g, "_")} rdf:type owl:NamedIndividual ,
                      :Pais ;
            ${countryString}
      }
    `
    // Make POST request to GraphDB
    const response = await axios.post(
      `${graphdbEndpoint}/statements`,
      sparqlQuery,
      {
        headers: {
          "Content-Type": "application/sparql-update",
          Accept: "application/sparql-results+json",
        },
      },
    )
    return response
  } catch (error: any) {
    console.error("Error making SPARQL query:", error.message) // Log error message
    if (error.response) {
      console.error("Response data:", error.response.data) // Log response data
      console.error("Response status:", error.response.status) // Log response status
      console.error("Response headers:", error.response.headers) // Log response headers
    } else if (error.request) {
      console.error("No response received:", error.request) // Log no response error
    } else {
      console.error("Error message:", error.message) // Log general error message
    }
    return null
  }
}
