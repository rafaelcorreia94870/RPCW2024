"use client"

import React, { useEffect, useState } from "react"
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/shadcn/resizable"
import { Button } from "../shadcn/button"
import WorldMap from "./world-map"
import SearchAutocomplete from "./search-autocomplete"
import CursorAnimation from "../misc/cursor-animation"
import { AllGuesses } from "../guess-card/all-guesses"
import { CountryData } from "@/lib/utils"
import { TileProps } from "../guess-card/tile"

interface SearchCountryProps {
  targetCountry: CountryData
  gameHints: TileProps["type"][]
}

export const SearchCountry = ({
  targetCountry,
  gameHints,
  }: SearchCountryProps) => {
    const [countryDataList, setCountryDataList] = useState<CountryData[]>([])
    const [buttonDisabled, setButtonDisabled] = useState(false)
    const [selectedName, setSelectedName] = useState("")

  const handleSelect = (name: string) => {
    setSelectedName(name)
    console.log("Selected name:", name)
  }

  useEffect(() => {
    if (countryDataList.some((data) => data.nome[0] === selectedName)) {
      setButtonDisabled(true)
    } else {
      setButtonDisabled(false)
    }
  }, [selectedName, countryDataList])

  const handleButtonClick = async () => {
    if (!selectedName || buttonDisabled) return

    try {
      const correctedName = selectedName.replace(/&/g, "and")
      const res = await fetch(`/api/country?country=${correctedName}`)
      const data: CountryData = await res.json()
      console.log("Fetched country data:", data)
      setCountryDataList((prevList) => [data, ...prevList])
    } catch (error) {
      console.error("Error fetching country data:", error)
    }
  }

  const guessedCountries = countryDataList.map((country) => country.nome[0])

  return (
    <>
      <ResizablePanelGroup direction="horizontal" className="min-h-[30rem]">
        <ResizablePanel defaultSize={75} minSize={40} maxSize={80}>
          <div className="flex h-full items-center justify-center p-6">
            <WorldMap
              onCountrySelect={setSelectedName}
              guessedCountries={guessedCountries}
            />
          </div>
        </ResizablePanel>
        <ResizableHandle withHandle className="z-0" />
        <ResizablePanel defaultSize={25} minSize={20} maxSize={60}>
          <div className="relative flex h-full w-full flex-col items-center justify-between p-6">
            <div className="w-full max-w-full">
              <SearchAutocomplete onSelect={handleSelect} />
            </div>
            <CursorAnimation
              source="search_animation"
              classes="relative flex w-full flex-col items-center"
            >
              <Button
                className={`h-[5rem] max-h-[5rem] w-[80%] max-w-[100%] text-wrap text-[100%] font-bold text-white ${buttonDisabled ? "" : "transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110"}`}
                onClick={handleButtonClick}
                disabled={buttonDisabled}
              >
                {buttonDisabled
                  ? "Try another one!"
                  : selectedName === ""
                    ? "Take a guess!"
                    : selectedName}
              </Button>
            </CursorAnimation>
          </div>
        </ResizablePanel>
      </ResizablePanelGroup>
      {countryDataList.length > 0 && (
        <AllGuesses
          countryDataList={countryDataList}
          gameHints={gameHints}
          targetCountry={targetCountry}
        />
      )}
    </>
  )
}
