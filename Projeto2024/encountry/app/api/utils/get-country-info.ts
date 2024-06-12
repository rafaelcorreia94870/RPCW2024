import axios from "axios"
import { graphdbEndpoint } from "./endpoint"
import { CountryData } from "@/lib/utils"


export async function getCountryInfo(
  country: string,
): Promise<CountryData | null> {
  const sparqlQuery = `
    PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
    SELECT ?verbo ?cena WHERE{
        ?country :nome "${country}".
        ?country a :Pais.
        ?country ?verbo ?cena MINUS {?country a ?cena}
    }
  `

  try {
    const response = await axios.get(graphdbEndpoint, {
      params: { query: sparqlQuery },
      headers: { Accept: "application/sparql-results+json" },
    })

    const countryInfo: Partial<CountryData> & { [key: string]: any } = {}
    for (let binding of response.data.results.bindings) {
      const verboURI = binding.verbo.value.split("/")
      const verbo = verboURI[verboURI.length - 1]
      if (verbo === "nome") {
        if (!(verbo in countryInfo)) {
          countryInfo[verbo] = []
        }
        ;(countryInfo[verbo] as string[]).push(binding.cena.value)
      } else {
        countryInfo[verbo] = binding.cena.value
      }
    }

    // Ensure that all properties exist, even if they are empty strings
    const completeCountryInfo: CountryData = {
      area: countryInfo.area || "",
      capital: countryInfo.capital || "",
      continente: countryInfo.continente || "",
      costa: countryInfo.costa || "",
      densidade_populacional: countryInfo.densidade_populacional || "",
      emissoes_co2: countryInfo.emissoes_co2 || "",
      espetativa_de_vida: countryInfo.espetativa_de_vida || "",
      exportacoes: countryInfo.exportacoes || "",
      flag: countryInfo.flag || "",
      gdp: countryInfo.gdp || "",
      hemisferio: countryInfo.hemisferio || "",
      importacoes: countryInfo.importacoes || "",
      lado_em_que_conduz: countryInfo.lado_em_que_conduz || "",
      latitude: countryInfo.latitude || "",
      literacia: countryInfo.literacia || "",
      longitude: countryInfo.longitude || "",
      medicos_por_mil: countryInfo.medicos_por_mil || "",
      migracao_liquida: countryInfo.migracao_liquida || "",
      moeda: countryInfo.moeda || "",
      mortalidade_infantil: countryInfo.mortalidade_infantil || "",
      nome: countryInfo.nome || [],
      populacao: countryInfo.populacao || "",
      racio_sexos: countryInfo.racio_sexos || "",
      receita_imposto: countryInfo.receita_imposto || "",
      taxa_de_mortalidade: countryInfo.taxa_de_mortalidade || "",
      taxa_de_natalidade: countryInfo.taxa_de_natalidade || "",
      taxa_desemprego: countryInfo.taxa_desemprego || "",
      taxa_fertilidade: countryInfo.taxa_fertilidade || "",
      telefones_por_1000: countryInfo.telefones_por_1000 || "",
      temperatura_media: countryInfo.temperatura_media || "",
    }

    return completeCountryInfo
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
