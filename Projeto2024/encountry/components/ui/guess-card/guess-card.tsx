import React, { useEffect, useState } from "react"
import Tile, { TileProps } from "./tile"
import { CountryData } from "@/lib/utils"
import GameEnd from "./game-end"
import {
  formatCurrency,
  isCurrencyString,
  isNumericString,
  roundNumber,
} from "./formatting-values"

interface GuessCardProps {
  selectedCountry: CountryData
  types: TileProps["type"][]
  targetCountry: CountryData
  comparisonCache: Record<string, Record<string, TileProps["hint"]>>
  updateComparisonCache: (
    key: string,
    data: Record<string, TileProps["hint"]>,
  ) => void
}

const GuessCard: React.FC<GuessCardProps> = ({
  selectedCountry,
  types,
  targetCountry,
  comparisonCache,
  updateComparisonCache,
}) => {
  const [hints, setHints] = useState<Record<string, TileProps["hint"]>>({})
  const [showDialog, setShowDialog] = useState(false)

  useEffect(() => {
    const cacheKey = `${selectedCountry.nome[0]}-${targetCountry.nome[0]}`

    const fetchData = async () => {
      if (comparisonCache[cacheKey]) {
        setHints(comparisonCache[cacheKey])
        checkAllRight(comparisonCache[cacheKey])
        return
      }

      try {
        const hintsData: Record<string, TileProps["hint"]> = {}
        for (const type of types) {
          const response = await fetch(
            `/api/compare?country1=${selectedCountry.nome[0]}&country2=${targetCountry.nome[0]}&row=${type}`,
          )
          const data = await response.json()
          hintsData[type] = data.result
        }
        setHints(hintsData)
        updateComparisonCache(cacheKey, hintsData)
        checkAllRight(hintsData)
      } catch (error) {
        console.error("Error fetching hints:", error)
      }
    }

    const checkAllRight = (hintsData: Record<string, TileProps["hint"]>) => {
      const allRight = Object.values(hintsData).every(
        (hint) => hint === "right",
      )
      if (allRight) {
        console.log("All guesses are right")
        setShowDialog(true)
      }
    }

    fetchData()
  }, [selectedCountry, targetCountry, types])

  const countryName = selectedCountry.nome[0]
  const countryFlag = selectedCountry.flag

  return (
    <>
      <div className="flex h-auto w-[70%] min-w-[30em] flex-col items-center gap-3 rounded-[3em] bg-card px-14 py-5 transition delay-150 ease-in-out hover:bg-stone-200 dark:hover:bg-neutral-800 md:flex-row md:justify-around">
        <div className="flex w-[40%] flex-col content-center justify-center gap-4">
          <div className="custom-font content-center bg-clip-text text-center text-[150%] font-normal tracking-wider text-card-foreground drop-shadow-lg md:text-[200%]">
            {countryName}
          </div>
          <div className="relative flex content-center justify-center rounded-md text-center transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110">
            <img
              src={countryFlag}
              alt={`${countryName} flag`}
              className="h-auto w-16 rounded-sm drop-shadow-lg"
            />
          </div>
        </div>
        <div className="flex h-auto w-full flex-shrink flex-row items-center justify-center gap-4">
          {types.map((type) => (
            <Tile
              key={type}
              type={type}
              hint={hints[type] === undefined ? "wrong" : hints[type]}
            >
              {type !== "nome"
                ? isCurrencyString(selectedCountry[type])
                  ? formatCurrency(selectedCountry[type])
                  : isNumericString(selectedCountry[type])
                    ? roundNumber(selectedCountry[type])
                    : selectedCountry[type]
                : undefined}
            </Tile>
          ))}
        </div>
      </div>

      {showDialog && <GameEnd countryName={countryName} />}
    </>
  )
}

export default GuessCard
