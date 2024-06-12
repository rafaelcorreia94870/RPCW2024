import { useEffect, useState } from "react"
import { Button } from "@/components/ui/shadcn/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/shadcn/dialog"
import { Input } from "@/components/ui/shadcn/input"
import { Label } from "@/components/ui/shadcn/label"
import { CountryDataEdit } from "@/lib/utils"
import { keyMappings } from "./ui/guess-card/tile-icon"
import SearchAutocomplete from "./ui/pick-country/search-autocomplete"
import * as HoverCard from "@radix-ui/react-hover-card"
import styles from "./ui/guess-card/hovercard.module.css"
import { AlertCircle } from "lucide-react"

import {
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/shadcn/alert"

interface CountryDialogProps {
  action: "Add" | "Edit" | "Remove"
  countryName?: string | null
}

export const CountryDialog = ({ action, countryName }: CountryDialogProps) => {
  const initialData: CountryDataEdit = {
    nome: "",
    continente: "",
    area: "",
    capital: "",
    flag: "",
    densidade_populacional: "",
    espetativa_de_vida: "",
    exportacoes: "",
    gdp: "",
    hemisferio: "",
    importacoes: "",
    lado_em_que_conduz: "",
    latitude: "",
    literacia: "",
    longitude: "",
    migracao_liquida: "",
    moeda: "",
    mortalidade_infantil: "",
    populacao: "",
    taxa_de_mortalidade: "",
    taxa_de_natalidade: "",
    telefones_por_1000: "",
    costa: "",
    temperatura_media: "",
    racio_sexos: "",
    taxa_desemprego: "",
    taxa_fertilidade: "",
    medicos_por_mil: "",
    receita_imposto: "",
    emissoes_co2: "",
  }

  const [formData, setFormData] = useState<CountryDataEdit>(initialData)
  const [selectedName, setSelectedName] = useState("")
  const [isDialogOpen, setIsDialogOpen] = useState(false)
  const [confirmationMessage, setConfirmationMessage] = useState<string | null>(
    null,
  )
  const [alertType, setAlertType] = useState<string>("")

  const handleSelect = (name: string) => {
    setSelectedName(name)
    console.log("Selected name:", name)
  }

  useEffect(() => {
    if (!countryName) return

    const fetchCountryData = async () => {
      try {
        const response = await fetch(`/api/country?country=${countryName}`)
        if (!response.ok) {
          throw new Error("Failed to fetch country information")
        }
        const data: CountryDataEdit = await response.json()
        setFormData(data)
      } catch (error: any) {
        console.error("Failed to fetch country data:", error.message)
      }
    }

    fetchCountryData()
  }, [countryName])

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { id, value } = e.target
    setFormData((prevData) => ({
      ...prevData,
      [id]: value,
    }))
  }

  const handleSubmit = async () => {
    try {
      let response: Response | undefined

      if (action === "Add") {
        response = await fetch("/api/country", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ country: formData }),
        })
      } else if (action === "Edit") {
        response = await fetch("/api/country", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ country: formData }),
        })
      } else if (action === "Remove") {
        if (countryName) setSelectedName(countryName)
        response = await fetch(`/api/country?country=${selectedName}`, {
          method: "DELETE",
        })
      }

      if (!response || !response.ok) {
        throw new Error(`Failed to ${action.toLowerCase()} country`)
      }

      const data = await response.json()
      console.log(`${action} successful`, data)

      // Show confirmation message and close the dialog
      setConfirmationMessage(
        `${selectedName} was sucessfully ${action.toLowerCase()}ed.`,
      )
      setAlertType("Success")
      setTimeout(() => {
        setIsDialogOpen(false)
        setAlertType("")
        setConfirmationMessage(null)
      }, 7000)
      if (action === "Remove" && countryName)
        window.location.href = "/countries"
      else window.location.reload()
    } catch (error: any) {
      console.error(`${action} error:`, error.message)
      // Handle error (e.g., show error message to the user)
      setConfirmationMessage(`There was an error removing ${selectedName}.`)
      setAlertType("Error")
      setTimeout(() => {
        setConfirmationMessage(null)
      }, 10000)
    }
  }

  return action === "Remove" && countryName ? (
    <>
      <Button type="button" variant="destructive" onClick={handleSubmit}>
        Remove
      </Button>
      {confirmationMessage && (
        <div className="fixed bottom-4 right-4 z-50 mb-6 mr-6">
          <Alert
            className="bg-background bg-opacity-35 backdrop-blur-md"
            variant={alertType === "Success" ? "success" : "destructive"}
          >
            {alertType === "Error" && <AlertCircle className="h-4 w-4" />}
            <AlertTitle className="font-extrabold">
              {alertType === "Success" ? alertType + "!" : alertType}
            </AlertTitle>
            <AlertDescription className="font-bold text-foreground">
              {confirmationMessage}
            </AlertDescription>
          </Alert>
        </div>
      )}
    </>
  ) : (
    <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
      <DialogTrigger asChild>
        <Button variant={action === "Remove" ? "destructive" : "default"}>
          {action}
        </Button>
      </DialogTrigger>
      <DialogContent
        className={`max-h-[80%] w-[70rem] overflow-hidden ${action === "Remove" ? "sm:max-w-[625px]" : "sm:max-w-[625px]"}`}
      >
        <DialogHeader className="sticky left-0 right-0 top-0 z-10 bg-opacity-20">
          <DialogTitle>{action} Country</DialogTitle>
          <DialogDescription>
            {action === "Remove"
              ? "Are you sure you want to remove this country?"
              : `Please ${action.toLowerCase()} the country details.`}
          </DialogDescription>
        </DialogHeader>
        <div
          className={`mtb-10 ${action === "Remove" ? "h-[35vh]" : "h-[50vh] overflow-y-auto scrollbar scrollbar-track-card scrollbar-thumb-muted scrollbar-thumb-rounded-full hover:cursor-pointer hover:scrollbar-thumb-border active:scrollbar-thumb-primary dark:hover:scrollbar-thumb-zinc-700"}`}
        >
          <div
            className={`${action === "Remove" ? "relative flex h-full w-full items-start justify-center" : "grid gap-4"} mx-4 py-4`}
          >
            {action === "Remove" ? (
              <div className="z-auto w-[80%] max-w-full">
                <SearchAutocomplete onSelect={handleSelect} />
              </div>
            ) : (
              Object.keys(initialData).map((key) => (
                <div key={key} className="grid grid-cols-4 items-center gap-6">
                  <Label htmlFor={key} className="text-right">
                    {keyMappings[key]}
                  </Label>
                  <Input
                    type="text"
                    id={key}
                    value={formData[key as keyof CountryDataEdit]}
                    onChange={handleChange}
                    className="col-span-3"
                  />
                </div>
              ))
            )}
          </div>
        </div>
        <DialogFooter className="sticky bottom-0 left-0 right-0 z-10 flex items-center justify-between gap-6">
          {confirmationMessage && (
            <Alert
              variant={alertType === "Success" ? "success" : "destructive"}
            >
              {alertType === "Error" && <AlertCircle className="h-4 w-4" />}
              <AlertTitle className="font-extrabold">
                {alertType === "Success" ? alertType + "!" : alertType}
              </AlertTitle>
              <AlertDescription className="text-red font-normal">
                {confirmationMessage}
              </AlertDescription>
            </Alert>
          )}
          <Button
            type="button"
            variant={action === "Remove" ? "destructive" : "default"}
            onClick={handleSubmit}
          >
            {action === "Remove" ? `Delete ${selectedName}` : "Save changes"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
