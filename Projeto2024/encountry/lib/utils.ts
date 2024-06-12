import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export interface CountryData {
  area: string
  capital: string
  continente: string
  costa: string
  densidade_populacional: string
  emissoes_co2: string
  espetativa_de_vida: string
  exportacoes: string
  flag: string
  gdp: string
  hemisferio: string
  importacoes: string
  lado_em_que_conduz: string
  latitude: string
  literacia: string
  longitude: string
  medicos_por_mil: string
  migracao_liquida: string
  moeda: string
  mortalidade_infantil: string
  nome: string[]
  populacao: string
  racio_sexos: string
  receita_imposto: string
  taxa_de_mortalidade: string
  taxa_de_natalidade: string
  taxa_desemprego: string
  taxa_fertilidade: string
  telefones_por_1000: string
  temperatura_media: string
}

export interface CountryDataEdit {
  area?: string
  capital?: string
  continente?: string
  costa?: string
  densidade_populacional?: string
  emissoes_co2?: string
  espetativa_de_vida?: string
  exportacoes?: string
  flag: string
  gdp?: string
  hemisferio?: string
  importacoes?: string
  lado_em_que_conduz?: string
  latitude?: string
  literacia?: string
  longitude?: string
  medicos_por_mil?: string
  migracao_liquida?: string
  moeda?: string
  mortalidade_infantil?: string
  nome: string
  populacao?: string
  racio_sexos?: string
  receita_imposto?: string
  taxa_de_mortalidade?: string
  taxa_de_natalidade?: string
  taxa_desemprego?: string
  taxa_fertilidade?: string
  telefones_por_1000?: string
  temperatura_media?: string
}
