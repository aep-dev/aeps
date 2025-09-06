---
title: The History and Philosophy of AEPs
date: 2025-02-03
authors:
  - name: Yusuke Tsutsumi
---

# The History and Philosophy of AEPs

There have been a lot of interest in the AEPs, and a question that often comes
up is "where did the AEPs come from?" and "what are the underlying motivation
and philosophies of the project?". This blog post aims to help answer those
questions.

## What are AEPs?

AEP is short for "API Enhancement Proposal", intended to be a comprehensive
specification, set of best practices, and tools to help an organization provide
best-in-class resource-oriented APIs.

More specifically, the following is provided:

1.  An API design specification for gRPC and REST APIs, with a heavy focus on
    [resource-oriented design](https://aep.dev/121/) and
    [standard methods](https://aep.dev/130/) that operate on them.

2.  Design patterns for common use cases such as
    [long-running operations](https://aep.dev/151/),
    [resource revisions](https://aep.dev/162/),
    [filtering](https://aep.dev/160/), with best practices aggregated from API
    design experts with experience at Google, Microsoft, Meta, Roblox, and
    DataBricks.

3.  An ecosystem of
    [server-side and client-side tooling](https://aep.dev/tooling-and-ecosystem/)
    to produce and consume AEP-compliant APIs.

## How did the AEPs begin?

The history of AEPs begin with the AIPs:
[Google API Improvement Proposals](https://google.aip.dev/): a set of design
patterns for resource-oriented APIs, focusing primarily on protobuf. AIPs
themselves were then open sourcing of internal documentation around Google
API's best practices.

Along with Google's own design practices, aip.dev also had a generic industry
wide component, that primarily focused on the idea of creating design style
guides that tailor to an organization's own needs. This project includes
components such as a
[style guide site generator](https://github.com/aip-dev/site-generator) as well
as a template of [more generic guidance](https://github.com/aip-dev/aip.dev).

Although aip.dev is not a formal API specification, an ecosystem of tooling
does exist that adheres to it, including:

- A protobuf based [api-linter](https://linter.aip.dev/).

- A [client library generator](https://github.com/googleapis/gapic-generator).

Among the contributors to aip.dev, some wanted to see a stronger formalization
of the API design guidance itself, for a few reasons:

1.  To act as a reference point for organization-agnostic best practices.

2.  To enable an official ecosystem of tooling to make best-practice APIs
    easier to build and consume.

This group forked aip.dev and created aep.dev. Since its founding in 2023,
aep.dev has rapidly progressed in building out a tooling ecosystem, and proving
that well-designed APIs can truly enable a simple-to-maintain but powerful
ecosystem of tooling
([read more here](https://aep.dev/tooling-and-ecosystem/)).

## What philosophies drive aep.dev?

### Adopting and sharing resource-oriented API best practices

We do not want to reinvent the wheel. Instead, our guidance is based on IETF
RFCs that exist around HTTP semantics, using them when applicable.

### Powerful server-side and client-side tooling, enabled by simple, consistent APIs.

As organizations develop their APIs, organizations must often create their own
service generators to create consistency, as well as create client-side tooling
to consume them. This includes:

- Linters and style guide checkers to ensure API consistency

- server-side generators, handling the creation of boilerplate interfaces that
  enable common features that include: CRUD of basic resources, pagination and
  filtering for lists, precondition checking, and documentation generation.

- Clients that interface with these APIs, including: SDKs, command line
  interface, web-based UIs, asset inventories.

Rather than have every organization create their own clients, AEPs strive to
provide the above tools, allowing an organization to focus on their goal and
from having to have full teams dedicated to maintaining these tools.

## Where to learn more?

Now that you have an understanding of the aeps, we encourage you to
[explore the project](https://aep.dev/), use the
[specification](https://aep.dev/1/) to help guide your APIs, and use the
[tooling](https://aep.dev/tooling-and-ecosystem/) to help produce and consume
them. Visit the [home page](https://aep.dev/) for more information!
