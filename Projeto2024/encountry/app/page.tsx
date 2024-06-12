"use client"

import React, { useState, useEffect } from "react"
import Header from "@/components/header"
import Game, { GameProps } from "@/components/game"
import { getRandomColumns } from "./api/utils/get-random-columns"
import { TileProps } from "@/components/ui/guess-card/tile"

const Home: React.FC = () => {
  const [targetCountry, setTargetCountry] =
    useState<GameProps["targetCountry"]>(null)
  const [error, setError] = useState<GameProps["error"]>(null)
  const [gameHints, setGameHints] = useState<TileProps["type"][]>([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch all country names from the API route
        const response = await fetch("/api/game")
        if (!response.ok) {
          throw new Error("Failed to fetch countries")
        } else {
          setTargetCountry(await response.json())
        }
      } catch (err) {
        console.error("Error fetching country data:", err)
        setError("Internal Server Error")
      }
    }
    setGameHints(getRandomColumns())
    fetchData()
  }, [])

  return (
    <>
      <Header targetCountry={targetCountry} />
      <Game targetCountry={targetCountry} error={error} gameHints={gameHints} />
    </>
  )
}

export default Home
