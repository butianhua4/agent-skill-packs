# Filled Sample: AI Workflow Log Debug Report

This sample uses fictional, redacted data. It is designed as buyer-facing proof
for the `ai-workflow-log-debug-skill` pack.

## Summary

The workflow stopped before the delivery email because the `create_invoice` tool
was called five times without a required `customer_id`. The agent had the
customer email and order total, but the lookup step that should map email to
customer ID either did not run or returned an empty result. This is a data
handoff failure, not a general model failure.

## Evidence

- `tool_call: create_invoice`
- `error: missing required field customer_id`
- `retry_count: 5`
- `available_fields: email, order_total, plan_name`
- `result: workflow stopped before delivery email`
- No successful `lookup_customer` result appears before invoice creation.

## Likely Root Cause

**Root cause:** the agent is calling the invoice tool before confirming that the
customer lookup step produced a valid ID.

**Confidence:** high.

The repeated retries are also increasing risk because the agent repeats the same
invalid call instead of switching to a missing-data branch.

## Risk Level

Medium.

The workflow is not creating invoices, but the retry behavior can waste tool
calls, confuse operators, and hide the true missing-data issue.

## Recommended Fix

1. Add a preflight check before `create_invoice`:
   - If `customer_id` exists, continue.
   - If `customer_id` is missing but email exists, run `lookup_customer`.
   - If lookup fails, stop and request a customer match instead of retrying the
     invoice tool.
2. Add a retry rule:
   - Do not retry `create_invoice` with identical missing fields.
   - Route repeated validation errors to a human-readable failure message.
3. Add logging fields:
   - `step_name`
   - `required_field`
   - `available_fields`
   - `lookup_result`
   - `next_safe_action`
4. Validate with two redacted fixtures:
   - Known customer email -> invoice is created.
   - Unknown customer email -> workflow stops with a clear missing-customer
     message.

## Customer Action Needed

- Provide a redacted example payload where the workflow succeeds.
- Provide a redacted example payload where the customer lookup fails.
- Confirm whether customer matching should use email only or email plus company
  name.

Do not send passwords, tokens, cookies, payment details, ID documents, or private
customer data.

## Validation

Recommended validation:

```text
Fixture A: email maps to customer_id
Expected: create_invoice receives customer_id and succeeds

Fixture B: email does not map to customer_id
Expected: create_invoice is not called; workflow returns missing-customer action

Fixture C: customer_id missing after lookup
Expected: zero repeated identical invoice retries
```

## Buyer-Facing Delivery Note

I found the failure point: the agent is trying to create an invoice before it has
a valid customer ID. I recommend adding a preflight customer lookup gate and a
stop rule for repeated missing-field retries. This will make the workflow fail
clearly when customer matching is incomplete, instead of looping on the same bad
tool call.
