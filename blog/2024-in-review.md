---
title: AEP's 2024 Year in Review
date: 2024-12-19
authors:
  - name: Mak Ahmad
  - name: Alex Stephen
  - name: Yusuke Tsutsumi
---

# Building Better APIs Together: AEP's 2024 Year in Review

As we close out 2024, we want to share the significant strides the API
Enhancement Proposals (AEP) project has made in creating a more cohesive API
ecosystem. What started as a fork of Google's API Improvement Proposals has
evolved into something much more ambitious: an open, community-driven standard
for building resource-oriented APIs that work consistently across different
protocols and platforms.

A brief summary of the achievements outlined below are:

- The creation of aepc, an AEP "compiler" that takes a succinct resource
  definition and generates protobuf and OpenAPI schemas.
- The 0.1 release of aepcli, which can consume aep-compliant APIs and generate
  a resource-oriented command-line-interfaces dynamically.
- A complete linter for protobuf APIs, and starting an OAS variant.
- aep-explorer: a prototype of a WEB UI to explore aep-compliant APIs.
- A redesigned website (aep.dev), where this blog post is published!

## The Vision Takes Shape

This year clarified our core belief that API design shouldn't be a bikeshedding
honeypot. By collecting hard-won design patterns from across the industry,
we've worked to narrow the decisions API producers need to make while improving
the experience for API consumers. Our approach focuses on resource-oriented
design principles that can be expressed in both Protocol Buffers and OpenAPI,
making AEPs protocol-agnostic while maintaining strong opinions about what
makes APIs more usable and maintainable.

## Major Technical Achievements

### aepc: The AEP compiler

We introduced [aepc](https://github.com/aep-dev/aepc), our service compiler
that transforms concise resource definitions into fully-specified APIs. With
just a few dozen lines of YAML describing your resources and their
relationships, aepc generates complete Protocol Buffer and OpenAPI
specifications that adhere to AEP standards. This dramatically reduces the
boilerplate needed to create consistent APIs while enforcing best practices
through generation rather than just validation.

aepc is just a prototype with no official release at this moment, but it has
been very useful, producing AEP-compliant OpenAPI and protobuf specifications
that are used as examples in the specification.

### aepcli: A Command-Line Interface for Everyone

The launch of version 0.1 of [aepcli](https://github.com/aep-dev/aepcli) marked
a significant milestone in our tooling journey. Rather than requiring every API
provider to build their own CLI, aepcli dynamically generates a powerful
command-line interface from any AEP-compliant API's OpenAPI specification. This
client-side approach means new API features are immediately available without
requiring CLI updates, solving a common pain point in API tooling.

### aep-explorer

To complement our command-line tools, we developed a web-based UI for browsing
and interacting with AEP-compliant APIs:
[aep-explorer](https://github.com/aep-dev/aep-explorer) . This provides a more
visual way to understand and experiment with APIs while maintaining the same
consistent interaction patterns that make AEPs valuable.

### Enhanced Linting Capabilities

A major focus this year was improving our linting capabilities, particularly
for OpenAPI specifications. Mike Kistler led the effort to revitalize our
[OpenAPI linter](https://github.com/aep-dev/aep-openapi-linter), implementing
rules for key AEPs including AEP-132 (List methods) and AEP-135. The linter
helps teams validate their APIs against AEP guidance, catching common issues
early in the development process.

Significantly progress was also made for our
[protobuf linter](https://github.com/aep-dev/api-linter), which is now
compliant with all of the updated guidance in aep.dev.

The linter's approach balances pragmatism with standards enforcement \- while
some rules are mandatory, others can be selectively adopted based on an
organization's needs. This flexibility helps teams gradually adopt AEP
practices while maintaining consistent APIs. The project uses Spectral as its
foundation, allowing teams to build on an established tooling ecosystem while
adding AEP-specific validations.

To help teams get started, we've included comprehensive test cases and example
APIs that demonstrate proper implementation of AEP patterns. The linter has
already helped identify areas where our documentation needed clarification,
particularly around operation IDs and resource naming conventions.

### Improved Infrastructure

A major focus this year was improving the components used for learning about
the AEP standards and enforcing them in our organization.

To help teams get started, we've built comprehensive test cases and example
APIs that demonstrate proper implementation of AEP patterns. The linters have
already helped identify areas where our documentation needed clarification,
particularly around operation IDs and resource naming conventions.

Additionally, we've built out a new aep.dev website based on a new framework to
help highlight our guidance and to help the team release new content over time.

## Community Growth

### The March Barn Raising

On Pi Day (March 14), we held our first community "barn raising" event,
bringing together contributors from across companies and time zones. The event
focused on improving documentation, adding OpenAPI examples, and making AEPs
more accessible to newcomers. This collaborative effort helped us identify and
address gaps in our guidance while strengthening our community bonds.

### Expanding Global Reach

Recognizing our growing international community, we established EU-friendly
meeting times and welcomed contributors from companies like DoubleVerify,
providing valuable feedback on real-world AEP adoption. This led to
improvements in our documentation and examples, particularly around pagination
and custom methods.

### Educational Content

We launched the [@aepdev](https://www.youtube.com/@aepdev) YouTube channel
featuring detailed demonstrations of our tooling and explanations of AEP
concepts. These videos help newcomers understand both the technical details and
the broader vision of what we're building.

## Looking Forward to 2025

As we enter the new year, our focus areas include:

1. Expanding our linting tools across both Protocol Buffer and OpenAPI
   specifications
2. Building more client generators, including Terraform providers and
   Kubernetes operators
3. Working with the OpenAPI community on resource-oriented API patterns
4. Supporting more companies in adopting AEPs, with clear migration paths and
   tooling support

## Get Involved

We're building AEPs in the open and welcome contributions of all kinds. You can
join us:

- On CNCF Slack in the \#aep channel
- At our weekly community meetings (Fridays at 11:30am PT)
- On GitHub at [github.com/aep-dev](https://github.com/aep-dev)
- Through our documentation at [aep.dev](https://aep.dev)

Whether you're building new APIs or working to improve existing ones, we
believe AEPs can help make that process more consistent and maintainable. Join
us in building better APIs together\!
