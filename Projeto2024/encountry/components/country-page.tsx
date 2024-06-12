"use client"

import { useEffect, useState } from "react"
import { useParams } from "next/navigation"
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/shadcn/table"
import { CountryData } from "@/lib/utils"
import { keyMappings } from "./ui/guess-card/tile-icon"

const CountryPage = () => {
  const [countryData, setCountryData] = useState<CountryData | null>(null)
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)
  const { country } = useParams()

  useEffect(() => {
    if (!country) return

    const fetchCountryData = async () => {
      try {
        const response = await fetch(`/api/country?country=${country}`)
        if (!response.ok) {
          throw new Error("Failed to fetch country information")
        }
        const data: CountryData = await response.json()
        setCountryData(data)
      } catch (error: any) {
        setError(error.message)
      } finally {
        setLoading(false)
      }
    }

    fetchCountryData()
  }, [country])

  if (loading)
    return (
      <div className="text-md flex min-h-[30rem] flex-col content-center items-center justify-center text-center text-muted-foreground">
        <span className="border-l-3 block h-10 w-10 animate-spin rounded-full border-b-2 border-muted-foreground"></span>
        <p className="my-4 text-lg text-muted-foreground">
          Fetching country data... Please wait.
        </p>
      </div>
    )

  if (error)
    return (
      <div className="flex min-h-[30rem] flex-col content-center items-center justify-center text-center text-2xl text-muted-foreground">
        Error! {error}
      </div>
    )

  if (!countryData)
    return (
      <div className="flex min-h-[30rem] flex-col content-center items-center justify-center text-center text-2xl text-muted-foreground">
        No data available.
      </div>
    )

  const countryAttributes = Object.entries(countryData)

  return (
    <div className="container mx-auto py-10">
      <div className="mb-4 flex items-center">
        <img
          src={countryData.flag}
          alt={`${countryData.nome[0]} flag`}
          className="mr-4 h-12 w-20 object-contain"
        />
        <h1 className="text-4xl font-bold">{countryData.nome[0]}</h1>
      </div>
      <div className="overflow-x-auto">
        <Table className="min-w-full">
          <TableCaption>Country Information</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>Attribute</TableHead>
              <TableHead>Value</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {countryAttributes.map(([key, value]) => (
              <TableRow key={key}>
                <TableCell className="border-b px-4 py-2">
                  {keyMappings[key] || key}
                </TableCell>
                <TableCell className="border-b px-4 py-2">
                  {Array.isArray(value) ? value.join(", ") : value}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}

export default CountryPage
