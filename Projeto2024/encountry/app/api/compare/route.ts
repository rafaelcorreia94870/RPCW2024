import { NextRequest, NextResponse } from "next/server"
import { compareCountries } from "../utils/compare-countries"

export async function GET(req: NextRequest) {
  const country1 = req.nextUrl.searchParams.get("country1")
  const country2 = req.nextUrl.searchParams.get("country2")
  const row = req.nextUrl.searchParams.get("row")

  if (!country1 || !country2 || !row) {
    return NextResponse.json(
      { error: "Country names and row are required" },
      { status: 400 },
    )
  }

  try {
    const comparisonResult = await compareCountries(country1, country2, row)
    if (comparisonResult) {
      return NextResponse.json({ result: comparisonResult }, { status: 200 })
    } else {
      return NextResponse.json(
        { error: "Failed to compare countries" },
        { status: 500 },
      )
    }
  } catch (error) {
    console.error("Error comparing countries:", error)
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}
