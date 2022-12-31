# Access Control

![access-control](https://user-images.githubusercontent.com/87711310/210135886-3c11468e-dd98-4fb0-abc3-cd9196684a1e.svg)


## What is access control?
Access control (or authorization) is the application of constraints on who (or what) can perform attempted actions or access resources that they have requested. In the context of web applications, access control is dependent on authentication and session management:

- Authentication identifies the user and confirms that they are who they say they are.
- Session management identifies which subsequent HTTP requests are being made by that same user.
- Access control determines whether the user is allowed to carry out the action that they are attempting to perform.

Broken access controls are a commonly encountered and often critical security vulnerability. Design and management of access controls is a complex and dynamic problem that applies business, organizational, and legal constraints to a technical implementation. Access control design decisions have to be made by humans, not technology, and the potential for errors is high.

From a user perspective, access controls can be divided into the following categories:

- Vertical access controls
- Horizontal access controls
- Context-dependent access controls

## Vertical access controls
Vertical access controls are mechanisms that restrict access to sensitive functionality that is not available to other types of users.

#### Vertical privelege escalation

When a user is able to gain access to a role or user they should not have access to.  A simple example is gaining access to the admin panel.  Types are:

- `Unprotected functionality`: insufficient access control on a resource and relies on that resource being hidden (e.g. admin panel does not check if the request is for an authenticated administrator).
- `Parameter based access control`: when a user is able to provide a parameter that escalates their privileges (e.g. `?admin=true` on a request).
-  `Platform misconfiguration`: allow access to protected resources via unexecpted HTTP methods (e.g. `PUT` or `DELETE` instead of an expected `POST` or `GET`).

## Horizontal access controls
Horizontal access controls are mechanisms that restrict access to resources to the users who are specifically allowed to access those resources.

#### Horizontal privilege escalation

When a user gains access to another user's data or resources.  

This can often be turned into a vertical privilege escalation by compromising a more priveleged user and then using that user to grant access to the attacker's account or create another privileged user account controlled by the attacker.

#### Insecure director object reference

When an attacker can directly access objects through input they supply.  This can include:

- Direct access to databaes objects through a user-supplied ID (e.g. `?id=1`).
- Direct access to filesystem objects by altering the URL (e.g. `?imageUrl=../../../ect/passwd`).


## Context-dependent access controls
Context-dependent access controls restrict access to functionality and resources based upon the state of the application or the user's interaction with it.

#### Access control vulnerabilities in multi-step processes

When a user is able to bypass sections of a multi-step process, which can occur whena access controls are not applied consistently to all steps.

#### Referer based access control

When an application relies on the `Referer` HTTP header to enforce access control.  Since this can be altered in the request, it allows for access control bypass.

An example could be if a page like `/admin/deleteUser` only checks for `Referer=admin` to perform access validation.

#### Location based access control

When ap application relies on geolocation IP lookup to enforce access control.  This can be circumvented with a VPN.


## Access control models

- `Programatic access control`: matrix of stored permissions that can be applied to users, groups or roles.  Permissions are applied before actions or access is performed to determine if it is allowed.
- `Discretional access control (DAC)`: users or groups are given access to resources and **can** grant access to other users/groups.
- `Mandatory access control (MAC)`: users or groups are given access to resources and **cannot** grant access to other users/groups.
- `Role-based access control (RBAC)`: users are assigned roles which are given access to resources.  A user can have multiple roles.

## Prevent

- Deny access by default to all resources.  Implement an allow-list for resources that are accessible.
- Use a single access control model for the entire application to prevent confusion.
- Have developers thoroughly declare all access requirements for each resource.
- Do not rely on obfustication or hiding of resources to prevent access.
- Rigorously test access control for all resources and actions, ideally using automation.
