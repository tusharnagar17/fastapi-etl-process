import FileUpload from "@/components/FileUpload"
import Image from "next/image"

export default function Home() {
    return (
        <main className="bg-lime-50 flex justify-center items-center min-h-screen">
            <FileUpload />
        </main>
    )
}
