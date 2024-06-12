"use client"

import React, { useEffect, useState } from "react"
import Link from "next/link"
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

const CountriesTable = () => {
  const [countriesData, setCountriesData] = useState<CountryData[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchCountries = async () => {
      try {
        const response = await fetch("/api/countries")
        if (!response.ok) {
          throw new Error("Failed to fetch countries")
        }
        const data: CountryData[] = await response.json()
        setCountriesData(data)
      } catch (error: any) {
        setError(error.message)
      } finally {
        setLoading(false)
      }
    }

    fetchCountries()
  }, [])

  if (loading)
    return (
      <div className="text-md flex min-h-[30rem] flex-col content-center items-center justify-center text-center text-muted-foreground">
        <span className="border-l-3 block h-10 w-10 animate-spin rounded-full border-b-2 border-muted-foreground"></span>
        <p className="my-4 text-lg text-muted-foreground">
          Getting all the countries... Please wait.
        </p>
      </div>
    )

  if (error)
    return (
      <div className="flex min-h-[30rem] flex-col content-center items-center justify-center text-center text-2xl text-muted-foreground">
        Error! {error}
      </div>
    )

  return (
    <Table className="px-10">
      <TableCaption>
        A list of all the countries in the United Nations.
      </TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Flag</TableHead>
          <TableHead>Area</TableHead>
          <TableHead>Population</TableHead>
          <TableHead>Capital</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {countriesData.map((country, index) => (
          <TableRow key={index}>
            <TableCell className="font-medium">
              <Link
                href={`/countries/${country.nome}`}
                className="hover:underline"
              >
                {country.nome}
              </Link>
            </TableCell>
            <TableCell>
              <img
                src={country.flag}
                alt={`${country.nome} flag`}
                className="h-12 w-20 object-contain"
              />
            </TableCell>
            <TableCell>{country.area}</TableCell>
            <TableCell>{country.populacao}</TableCell>
            <TableCell>{country.capital}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}

export default CountriesTable
