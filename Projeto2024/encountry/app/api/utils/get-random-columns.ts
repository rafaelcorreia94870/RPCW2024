import { TileProps } from "@/components/ui/guess-card/tile"

const rows_facil = [
  "continente",
  "hemisferio",
  "latitude",
  "longitude",
  "temperatura_media",
] as const
const rows_medio = [
  "gdp",
  "area",
  "densidade_populacional",
  "lado_em_que_conduz",
  "populacao",
] as const
const rows_dificil = [
  "taxa_desemprego",
  "taxa_fertilidade",
  "racio_sexos",
  "emissoes_co2",
  "telefones_por_1000",
  "taxa_de_natalidade",
  "taxa_de_mortalidade",
  "costa",
  "espetativa_de_vida",
  "exportacoes",
  "importacoes",
  "literacia",
  "migracao_liquida",
  "mortalidade_infantil",
] as const

function getRandomIndex(array: readonly string[]): number {
  return Math.floor(Math.random() * array.length)
}

export function getRandomColumns(): TileProps["type"][] {
  const columns: TileProps["type"][] = []

  const random1 = getRandomIndex(rows_facil)
  let random2 = getRandomIndex(rows_facil)
  while (random2 === random1) {
    random2 = getRandomIndex(rows_facil)
  }

  let random3 = getRandomIndex(rows_facil)
  while (random3 === random1 || random3 === random2) {
    random3 = getRandomIndex(rows_facil)
  }

  const random4 = getRandomIndex(rows_medio)
  const random5 = getRandomIndex(rows_dificil)

  columns.push(rows_facil[random1])
  columns.push(rows_facil[random2])
  columns.push(rows_facil[random3])
  columns.push(rows_medio[random4])
  columns.push(rows_dificil[random5])

  return columns
}
