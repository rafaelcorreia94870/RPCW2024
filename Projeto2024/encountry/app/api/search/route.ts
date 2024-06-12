import { NextRequest, NextResponse } from "next/server"

export async function GET(req: NextRequest) {
  const searchTerm = req.nextUrl.searchParams.get("searchTerm")

  if (!searchTerm) {
    return NextResponse.json(
      { error: "Search term is required" },
      { status: 400 },
    )
  }

  const query = `
    PREFIX : <http://www.rpcw.pt/rafa/ontologies/2024/paises/>
    SELECT (SAMPLE(?name) AS ?country) ?flag WHERE {
      ?c a :Pais.
      ?c :nome ?name.
      ?c :flag ?flag.
      FILTER(CONTAINS(LCASE(?name), "${searchTerm.toLowerCase()}"))
    } GROUP BY ?flag
  `
  const url = `http://localhost:7200/repositories/paises?query=${encodeURIComponent(query)}`

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Accept: "application/sparql-results+json",
      },
    })

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`)
    }

    const data = await response.json()
    return NextResponse.json(data.results.bindings, { status: 200 })
  } catch (error) {
    console.error("Error making SPARQL query:", error)
    return NextResponse.json({ error: "Failed to fetch data" }, { status: 500 })
  }
}
