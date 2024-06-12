import { NextRequest, NextResponse } from "next/server"
import { getCountryInfo } from "../utils/get-country-info"
import { CountryData, CountryDataEdit } from "@/lib/utils"
import { editCountry } from "../utils/edit-country"
import { deleteCountry } from "../utils/delete-country"
import { addCountry } from "../utils/add-country"

// GET route to fetch country information
export async function GET(req: NextRequest) {
  const country = req.nextUrl.searchParams.get("country")

  if (!country) {
    return NextResponse.json(
      { error: "Country name is required" },
      { status: 400 },
    )
  }

  try {
    const countryInfo = await getCountryInfo(country)
    if (countryInfo) {
      return NextResponse.json(countryInfo, { status: 200 })
    } else {
      return NextResponse.json(
        { error: "Failed to fetch country information" },
        { status: 500 },
      )
    }
  } catch (error) {
    console.error("Error fetching country information:", error)
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}

// POST route to edit country information
export async function POST(req: NextRequest) {
  try {
    const body = await req.json()
    const country: CountryDataEdit = body.country

    if (!country || !country.nome) {
      return NextResponse.json(
        { error: "Country data is required" },
        { status: 400 },
      )
    }

    const result = await editCountry(country)

    if (result && (result.status === 200 || result.status === 204)) {
      return NextResponse.json(
        { message: "Country information updated successfully" },
        { status: 200 },
      )
    } else {
      return NextResponse.json(
        { error: "Failed to update country information" },
        { status: 500 },
      )
    }
  } catch (error: any) {
    console.error("Error updating country information:", error)
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}

// DELETE route to delete country information
export async function DELETE(req: NextRequest) {
  try {
    const country = req.nextUrl.searchParams.get("country")

    if (!country) {
      return NextResponse.json(
        { error: "Country name is required" },
        { status: 400 },
      )
    }

    const result = await deleteCountry(country)

    if (result && (result.status === 200 || result.status === 204)) {
      return NextResponse.json(
        { message: "Country information deleted successfully" },
        { status: 200 },
      )
    } else {
      return NextResponse.json(
        { error: "Failed to delete country information" },
        { status: 500 },
      )
    }
  } catch (error: any) {
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}

// PUT route to add country information
export async function PUT(req: NextRequest) {
  try {
    const body = await req.json()

    const country: CountryDataEdit = body.country

    if (!country || !country.nome) {
      console.error("Validation failed: Country data is required") // Log validation error
      return NextResponse.json(
        { error: "Country data is required" },
        { status: 400 },
      )
    }

    const result = await addCountry(country)

    if (result && (result.status === 200 || result.status === 204)) {
      console.log("Result status:", result?.status)
      return NextResponse.json(
        { message: "Country information added successfully" },
        { status: 200 },
      )
    } else {
      console.error("Failed to add country information", result) // Log failure details
      return NextResponse.json(
        { error: "Failed to add country information" },
        { status: 500 },
      )
    }
  } catch (error: any) {
    console.error("Error adding country information:", error) // Log the error details
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    )
  }
}
