import axios from "axios"
import { graphdbEndpoint } from "./endpoint"
import { CountryData } from "@/lib/utils"

export async function getAllCountries(): Promise<string[]> {
  const sparqlQuery = `
    PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
    SELECT ?country_name WHERE{
        ?c a :Pais.
        ?c :nome ?country_name.
    }
  `

  try {
    const response = await axios.get(graphdbEndpoint, {
      params: { query: sparqlQuery },
      headers: { Accept: "application/sparql-results+json" },
    })

    const countries: string[] = []
    for (let binding of response.data.results.bindings) {
      countries.push(binding.country_name.value)
    }

    return countries
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
    return []
  }
}


export async function getAllCountriesInfo(): Promise<CountryData[]> {
  const sparqlQuery = `
  PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
SELECT ?c (SAMPLE(?name) AS ?nome) ?capital ?area ?populacao ?flag WHERE{
        ?c a :Pais;
         :nome ?name;
         :capital ?capital;
         :area ?area;
         :populacao ?populacao;
         :flag ?flag.
} GROUP BY ?c ?capital ?area ?populacao ?flag
  `

  try {
    const response = await axios.get(graphdbEndpoint, {
      params: { query: sparqlQuery },
      headers: { Accept: "application/sparql-results+json" },
    })

    const countries: CountryData[] = []
    for (let binding of response.data.results.bindings) {
      const completeCountryInfo: CountryData = {
        area: binding.area.value || "",
        capital: binding.capital.value || "",
        flag: binding.flag.value || "",
        nome: binding.nome.value || "",
        populacao: binding.populacao.value || "",
        continente: "",
        costa: "",
        densidade_populacional: "",
        emissoes_co2: "",
        espetativa_de_vida: "",
        exportacoes: "",
        gdp: "",
        hemisferio: "",
        importacoes: "",
        lado_em_que_conduz: "",
        latitude: "",
        literacia: "",
        longitude: "",
        medicos_por_mil: "",
        migracao_liquida: "",
        moeda: "",
        mortalidade_infantil: "",
        racio_sexos: "",
        receita_imposto: "",
        taxa_de_mortalidade: "",
        taxa_de_natalidade: "",
        taxa_desemprego: "",
        taxa_fertilidade: "",
        telefones_por_1000: "",
        temperatura_media: ""
      }
      countries.push(completeCountryInfo)
    }

    return countries
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
    return []
  }
}
