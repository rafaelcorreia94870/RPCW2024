// Check if a string is a numeric value after removing commas and spaces
export const isNumericString = (str: string) => {
  return !isNaN(Number(str.replace(/[,\s]/g, "")))
}

// Round a numeric string to M (millions), B (billions), etc.
export const roundNumber = (numStr: string) => {
  const num = parseFloat(numStr.replace(/[,\s]/g, "")) // Remove commas and spaces, then convert to number
  if (num >= 1e9) {
    return (num / 1e9).toFixed(1) + "B" // Billions
  } else if (num >= 1e6) {
    return (num / 1e6).toFixed(1) + "M" // Millions
  } else if (num >= 1e3) {
    return (num / 1e3).toFixed(1) + "K" // Thousands
  } else if (num % 1 !== 0) {
    return num.toFixed(2) // Floating-point numbers
  }
  return num.toString() // Return the number as a string if it's less than 1000 and not a float
}

// Handle currency formatting
export const formatCurrency = (str: string) => {
  const num = parseFloat(str.replace(/[^\d.-]/g, "")) // Remove non-numeric characters
  if (num >= 1e9) {
    return `$${(num / 1e9).toFixed(1)}B` // Billions
  } else if (num >= 1e6) {
    return `$${(num / 1e6).toFixed(1)}M` // Millions
  } else if (num >= 1e3) {
    return `$${(num / 1e3).toFixed(1)}K` // Thousands
  }
  return `$${num.toLocaleString(undefined, { maximumFractionDigits: 0 })}` // Less than 1000
}

// Check if a string is a currency value
export const isCurrencyString = (str: string) => {
  return /\$/.test(str)
}
