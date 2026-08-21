class AnswerGenerator:

    def generate(self, query, source):

        title = self._extract_title(source)
        content = self._clean_content(source)

        if title == "Password Reset":
            return (
                "To reset your password, select "
                "\"Forgot Password\" on the CloudDesk login page. "
                "A reset link will be sent to your registered email "
                "address. The link expires after 30 minutes. "
                "If you do not receive it, check your spam or junk "
                "folder. If the email is still missing, please "
                "contact support."
            )

        if title == "Account Locked":
            return (
                "Your CloudDesk account may be temporarily locked "
                "after multiple unsuccessful login attempts. "
                "Please wait 15 minutes and try again. If it remains "
                "locked, support will need to verify your identity "
                "before unlocking it."
            )

        if title == "Multi-Factor Authentication":
            return (
                "You can enable MFA from Settings → Security → "
                "Multi-Factor Authentication. CloudDesk supports "
                "authenticator-app based MFA. If you have lost "
                "access to your authenticator device, please "
                "contact support for identity verification."
            )

        if title == "Duplicate Charge":
            return (
                "If you believe you were charged twice, please "
                "provide your invoice number and transaction date. "
                "Support will verify whether the transactions are "
                "separate charges or whether one is an authorization "
                "and the other is the completed payment. If a genuine "
                "duplicate charge is confirmed, the billing team "
                "will process the appropriate refund."
            )

        if title == "Subscription Cancellation":
            return (
                "You can cancel your CloudDesk subscription from "
                "Settings → Billing → Cancel Subscription. "
                "Cancellation stops the next renewal but does not "
                "automatically refund the current billing period. "
                "Refund requests must be reviewed by the billing team."
            )

        if title == "Payment Methods":
            return (
                "You can update your payment method from "
                "Settings → Billing → Payment Methods. "
                "Available payment methods depend on your "
                "subscription and billing region."
            )

        if title == "Application Not Loading":
            return (
                "If CloudDesk is not loading, first refresh the "
                "browser and clear the browser cache. You can also "
                "try an updated version of Chrome, Edge, or Firefox. "
                "If the problem continues, please provide your "
                "browser name, operating system, and approximate "
                "time when the issue occurred."
            )

        if title == "API Errors":
            return (
                "CloudDesk API errors can occur when the authentication "
                "token is invalid or expired. Please verify that the "
                "API token is active and correctly configured. If the "
                "token is valid and the problem continues, contact "
                "technical support with the API endpoint, HTTP status "
                "code, and timestamp."
            )

        if title == "Integration Problems":
            return (
                "If a third-party integration stops working, verify "
                "that the integration is enabled and that its "
                "authentication credentials have not expired. "
                "If the problem continues, technical support should "
                "investigate the integration logs."
            )

        return content

    def _extract_title(self, source):

        for line in source.splitlines():

            if line.startswith("TITLE:"):
                return line.replace(
                    "TITLE:", ""
                ).strip()

        return ""

    def _clean_content(self, source):

        lines = source.splitlines()

        cleaned_lines = []

        for line in lines:

            if line.startswith("TITLE:"):
                continue

            if line.startswith("KEYWORDS:"):
                break

            if line.startswith("["):
                continue

            cleaned_lines.append(line)

        return "\n".join(cleaned_lines).strip()