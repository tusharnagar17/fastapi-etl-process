"use client"
import { UploadFileService } from "@/services/upload"
import React, { useState } from "react"

const FileUpload = ({ name }) => {
    const [paymentFile, setPaymentFile] =
        useState(null)
    const [merchantFile, setMerchantFile] =
        useState(null)

    const handlePaymentFileChange = (event) => {
        setPaymentFile(event.target.files[0])
    }

    const handleMerchantFileChange = (event) => {
        setMerchantFile(event.target.files[0])
    }

    const handleUpload = async () => {
        if (!paymentFile || !merchantFile) return

        const formData = new FormData()
        formData.append(
            "payment_report",
            paymentFile
        )
        formData.append(
            "merchant_report",
            merchantFile
        )

        // UploadFile service
        await UploadFileService(formData)

        setMerchantFile(null)
        setPaymentFile(null)
    }

    return (
        <div className="border p-20 flex flex-col items-center rounded-md shadow-lg bg-gray-100">
            {/* Merchant Report */}
            <div>
                <label
                    htmlFor="payment_report"
                    className="form-label"
                >
                    Payment Report
                </label>
                <br />
                <br />

                <input
                    type="file"
                    id="payment_report"
                    className="form-input"
                    onChange={
                        handlePaymentFileChange
                    }
                />
            </div>
            <br />
            <br />

            {/* Payment report */}
            <div>
                <label
                    htmlFor="merchant_report"
                    className="form-label"
                >
                    Merchant Report
                </label>
                <br />

                <br />
                <input
                    type="file"
                    id="merchant_report"
                    className="form-input"
                    onChange={
                        handleMerchantFileChange
                    }
                />
            </div>
            <br />
            <button
                type="button"
                onClick={() => handleUpload}
                className="w-2/4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 
                font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 
                focus:outline-none dark:focus:ring-blue-800"
            >
                Upload
            </button>
        </div>
    )
}

export default FileUpload
