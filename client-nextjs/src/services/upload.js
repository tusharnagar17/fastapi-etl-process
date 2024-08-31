import { SERVER_URL } from "."

export const UploadFileService = async (formData) => {
    try {
        const response = await fetch(`${SERVER_URL}/api/upload`, {
            method: "POST",
            body: formData,
        })

        if (response.ok) {
            const result = await response.json()
            console.log("File uploaded successfully", result)
        } else {
            console.error("Failed to upload file")
        }
    } catch (error) {
        console.error("Error uploading file:", error)
    }
}
