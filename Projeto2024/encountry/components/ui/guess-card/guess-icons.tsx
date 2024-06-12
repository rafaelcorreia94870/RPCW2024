import { FaPeopleGroup } from "react-icons/fa6" // populacao
import { IoResizeOutline } from "react-icons/io5" // area
import { MdFilterCenterFocus } from "react-icons/md" // capital
import { MdLocationCity } from "react-icons/md" // densidade_populacional
import { RiTimeLine } from "react-icons/ri" // espetativa_de_vida
import { CiExport } from "react-icons/ci" // exportacoes
import { TbWorldLatitude } from "react-icons/tb" // latitude
import { TbWorldLongitude } from "react-icons/tb" // longitude
import { PiGlobeHemisphereWestFill } from "react-icons/pi" // hemisferio
import { FaBookReader } from "react-icons/fa" // literacia
import { FaPersonWalkingLuggage } from "react-icons/fa6" // migracao_liquida
import { FaMoneyBillWave } from "react-icons/fa" // moeda
import { CiImport } from "react-icons/ci" // importacoes
import { MdDriveEta } from "react-icons/md" // lado_em_que_conduz
import { MdLocalPhone } from "react-icons/md" // telefones_por_1000
import { GiLighthouse } from "react-icons/gi" // costa
import { FaTemperatureHalf } from "react-icons/fa6" // temperatura_media
import { TbGenderBigender } from "react-icons/tb" //racio_sexos
import { FaPersonCircleMinus } from "react-icons/fa6" // taxa_desemprego
import { MdPregnantWoman } from "react-icons/md" // taxa_fertilidade
import { IoSkullOutline } from "react-icons/io5" // taxa_de_mortalidade
import { FaUserMd } from "react-icons/fa" // medicos_por_mil
import { LiaMoneyBillWaveSolid } from "react-icons/lia" // receita_imposto
import { FaCloudscale } from "react-icons/fa" // emissoes_co2
import { MdOutlineBedroomBaby } from "react-icons/md" // mortalidade_infantil
import { FaBaby } from "react-icons/fa" // taxa_de_natalidade

import { LuMountain, LuCoins } from "react-icons/lu"

import { TileProps } from "@/components/ui/guess-card/tile"

const getAdjustedSize = (baseSize: string, adjustment: number) => {
  const baseValue = parseFloat(baseSize)
  const adjustedValue = baseValue + adjustment
  return `${adjustedValue}%`
}

export const getIcon = (type: TileProps["type"]) => {
  const baseSize = 30
  const size = `${baseSize}%`
  const color = "foreground"

  switch (type) {
    case "populacao":
      return <FaPeopleGroup size={size} color={color} />
    case "temperatura_media":
      return (
        <FaTemperatureHalf size={getAdjustedSize(size, -10)} color={color} />
      )
    case "continente":
      return <LuMountain size={size} color={color} />
    case "gdp":
      return <LuCoins size={size} color={color} />
    case "latitude":
      return <TbWorldLatitude size={size} color={color} />
    case "longitude":
      return <TbWorldLongitude size={size} color={color} />
    case "area":
      return <IoResizeOutline size={size} color={color} />
    case "capital":
      return <MdLocationCity size={size} color={color} />
    case "hemisferio":
      return <PiGlobeHemisphereWestFill size={size} color={color} />
    case "densidade_populacional":
      return <MdFilterCenterFocus size={size} color={color} />
    case "espetativa_de_vida":
      return <RiTimeLine size={size} color={color} />
    case "exportacoes":
      return <CiExport size={size} color={color} />
    case "importacoes":
      return <CiImport size={size} color={color} />
    case "lado_em_que_conduz":
      return <MdDriveEta size={size} color={color} />
    case "literacia":
      return <FaBookReader size={getAdjustedSize(size, -3)} color={color} />
    case "migracao_liquida":
      return <FaPersonWalkingLuggage size={size} color={color} />
    case "moeda":
      return <FaMoneyBillWave size={size} color={color} />
    case "mortalidade_infantil":
      return <MdOutlineBedroomBaby size={size} color={color} />
    case "taxa_de_mortalidade":
      return <IoSkullOutline size={size} color={color} />
    case "taxa_de_natalidade":
      return <FaBaby size={getAdjustedSize(size, -7)} color={color} />
    case "telefones_por_1000":
      return <MdLocalPhone size={size} color={color} />
    case "costa":
      return <GiLighthouse size={size} color={color} />
    case "racio_sexos":
      return <TbGenderBigender size={size} color={color} />
    case "taxa_desemprego":
      return <FaPersonCircleMinus size={size} color={color} />
    case "taxa_fertilidade":
      return <MdPregnantWoman size={size} color={color} />
    case "medicos_por_mil":
      return <FaUserMd size={getAdjustedSize(size, -5)} color={color} />
    case "receita_imposto":
      return <LiaMoneyBillWaveSolid size={size} color={color} />
    case "emissoes_co2":
      return <FaCloudscale size={getAdjustedSize(size, -3)} color={color} />
    default:
      return null
  }
}
