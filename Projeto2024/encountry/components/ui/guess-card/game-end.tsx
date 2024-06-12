import React from "react"
import useWindowSize from "react-use/lib/useWindowSize"
import Confetti from "react-confetti"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from "@/components/ui/shadcn/dialog"
import { Button } from "../shadcn/button"
import CursorAnimation from "../misc/cursor-animation"

interface GameEndProps {
  countryName: string
}

const GameEnd = ({ countryName }: GameEndProps) => {
  const handleNewGame = () => {
    window.location.reload()
  }
  const { width, height } = useWindowSize()

  return (
    <Dialog open={true} defaultOpen={true}>
      <Confetti width={width} height={height + 1000} />
      <DialogContent className="flex flex-col content-center items-center justify-center">
        <DialogHeader>
          <DialogTitle>
            <CursorAnimation
              source="congrats"
              classes="font-extrabold text-3xl items-center"
            >
              Congratulations! 🎉
            </CursorAnimation>
          </DialogTitle>

          <DialogDescription className="flex flex-col items-center">
            You guessed the country:{" "}
            <span className="text-xl font-bold">{countryName}</span>
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className="sm:justify-start">
          <Button
            type="button"
            variant="secondary"
            onClick={() => (window.location.href = `/countries/${countryName}`)}
          >
            Learn more about {countryName}
          </Button>
          <Button
            type="button"
            variant="default"
            onClick={handleNewGame}
            className="font-bold"
          >
            New game!
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}

export default GameEnd
