import { NextResponse } from "next/server"
import { getAllCountries } from "../utils/get-all-countries"
import { getCountryInfo } from "../utils/get-country-info"

// Use a global variable to store the previously selected country
let previousCountry = ""

function seededRandom(seed: number) {
  var x = Math.sin(seed) * 10000
  return x - Math.floor(x)
}

export async function GET() {
  try {
    // Get all country names
    const countries = (await getAllCountries()) as string[]

    if (!countries || countries.length === 0) {
      return NextResponse.json({ error: "No countries found" }, { status: 404 })
    }

    // Generate a unique seed based on current time
    const seed = new Date().getTime()
    let randomIndex = Math.floor(seededRandom(seed) * countries.length)

    // Ensure the new country is not the same as the previous one
    while (countries[randomIndex] === previousCountry) {
      randomIndex = Math.floor(seededRandom(seed + 1) * countries.length)
    }

    // Pick a random country based on the generated index
    const randomCountry = countries[randomIndex]

    // Update the previous country
    previousCountry = randomCountry

    // Get detailed information about the selected country
    const countryInfo = await getCountryInfo(randomCountry)

    if (!countryInfo) {
      return NextResponse.json(
        { error: "Failed to get country info" },
        { status: 500 },
      )
    }

    // Return the detailed information as JSON
    return NextResponse.json(countryInfo)
  } catch (error: any) {
    console.error("Error:", error.message)
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}
