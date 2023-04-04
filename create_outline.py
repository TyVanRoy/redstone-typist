import sys
import os
from typing import List, Tuple
import openai_api as openai_api

# Ensure the OPENAI_API_KEY environment variable is set

outline_prompt = """
Please create an outline for the following TypeScript code. The outline should be a compressed version of the code, structured like the example below:

-----

// Imports with full paths
import { User } from "../models/user.model";
import { Authorization, PaymentMethod, PaymentMethodSetupIntent, RequestContext } from "../utils/types/common";
import * as permissionGuards from "../utils/permissions/guards";
import * as stripeServices from "../services/thirdparty/stripe/stripe.service";
import { generateAccessToken } from "../middleware/authorization.middleware";
import { logAction, logError } from "../utils/logger.util";
import { UserErrorMessage } from "../utils/enums/errorMessages";
import { ActionResult } from "../utils/enums/common";
import { UserSearchQuery } from "../utils/types/models";
import { Payment } from "models/payment.model";

// Any interfaces or types (if any in file)
// (already imported from "../utils/types/common")

// Any constants (if any in file)
// (none)

// Function signatures with parameters, return types, and comments (top-level and body)  (if any in file)

/**
 * Return the user with the given userId, or the user making the request if no userId is provided.
 * @param userId
 * @param context
 * @returns the user with eagerly-loaded fields
 */
export async function getUser(userId: number, context: RequestContext): Promise<User> {
    // Comments describing any side-effects of the function, if not specified in the function signature
    // Identity guard
}

/**
 * Updates the client user and profile with the given userId.
 * @param userId
 * @param update
 * @param context
 * @returns true if successful
 */
export async function updateUser(
    clientUserId: number,
    update: User,
    context: RequestContext
): Promise<boolean> {
    // Identity guard
}

// Class signatures with functions and field signatures, including comments (top-level and body) (if any in file)
// (none)

-----

Here's the full code:\n\n-----\n<<<file_content>>>\n-----\n
"""

# prompt = outline_prompt.format(file_content=file_content)


def create_prompt(file_content: str) -> str:
    prompt = outline_prompt.replace('<<<file_content>>>', file_content)
    return prompt


def generate_outline(input_file: str, output_file: str) -> None:
    with open(input_file, "r") as file:
        content = file.read()

    prompt = create_prompt(content)

    outline = openai_api.generate_response(
        prompt, tokens=1000, temperature=0.5)

    with open(output_file, "w") as file:
        file.write(outline)


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    generate_outline(input_file, output_file)
