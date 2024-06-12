import React, { useState } from "react"
import GuessCard from "./guess-card"
import { TileProps } from "./tile"
import { CountryData } from "@/lib/utils"


interface AllGuessesProps {
  countryDataList: CountryData[]
  gameHints: TileProps["type"][]
  targetCountry: CountryData
}

export const AllGuesses = ({
  countryDataList,
  gameHints,
  targetCountry,
}: AllGuessesProps) => {
  const [comparisonCache, setComparisonCache] = useState<
    Record<string, Record<string, TileProps["hint"]>>
  >({})

  const updateComparisonCache = (
    key: string,
    data: Record<string, TileProps["hint"]>,
  ) => {
    setComparisonCache((prevCache) => ({
      ...prevCache,
      [key]: data,
    }))
  }

  if (countryDataList.length === 0) {
    return (
      <div className="flex w-full flex-col items-center gap-5 py-10">
        No country data available.
      </div>
    )
  }

  return (
    <div className="flex w-full flex-col items-center gap-5 py-10">
      {countryDataList.reverse().map((countryData, index) => (
        <GuessCard
          key={index}
          selectedCountry={countryData}
          types={gameHints}
          targetCountry={targetCountry}
          comparisonCache={comparisonCache}
          updateComparisonCache={updateComparisonCache}
        />
      ))}
    </div>
  )
}

/*
const types1: TileProps["type"][] = [
    "area",
    "capital",
    "densidade_populacional",
    "espetativa_de_vida",
    "exportacoes",
  ]
  const types2: TileProps["type"][] = [
    "gdp",
    "hemisferio",
    "importacoes",
    "lado_em_que_conduz",
    "latitude",
  ]
  const types3: TileProps["type"][] = [
    "literacia",
    "longitude",
    "migracao_liquida",
    "moeda",
    "mortalidade_infantil",
  ]
  const types4: TileProps["type"][] = [
    "populacao",
    "taxa_de_mortalidade",
    "taxa_de_natalidade",
    "telefones_por_1000",
    "costa",
  ]
  const types5: TileProps["type"][] = [
    "temperatura_media",
    "racio_sexos",
    "taxa_desemprego",
    "taxa_fertilidade",
    "medicos_por_mil",
  ]
  const types6: TileProps["type"][] = [
    "receita_imposto",
    "emissoes_co2",
    "capital",
    "continente",
    "area",
  ]
*/
