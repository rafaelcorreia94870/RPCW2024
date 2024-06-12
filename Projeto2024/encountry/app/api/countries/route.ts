import { NextResponse } from "next/server"
import { getAllCountriesInfo } from "../utils/get-all-countries"
import { CountryData } from "@/lib/utils"

export async function GET() {
  try {
    // Get all country names
    const countriesData = await getAllCountriesInfo()

    // Filter out null values
    const filteredCountriesData = countriesData.filter(
      (country) => country !== null,
    ) as CountryData[]

    // Return the detailed information as JSON
    return NextResponse.json(filteredCountriesData)
  } catch (error: any) {
    console.error("Error:", error.message)
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}
