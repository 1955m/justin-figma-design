# Avatars

This folder is for approved avatar images **provided by the user**. Agents
must not generate avatar images. It starts empty by design.

## File conventions

- Prefer square PNG or WebP files with a practical UI resolution.
- Use non-personal names such as `avatar-01.png` or
  `avatar-role-admin.webp`.
- Do not include a person's name, email, customer ID, or private data in
  the filename or metadata.

## Figma usage

1. Check the target file for an existing avatar component first.
2. Import a user-provided file only after confirming it is safe to share.
3. Preserve aspect ratio and apply the target component's radius or mask.
4. Use an instance swap or image-fill property for reusable components.
5. Screenshot-check the crop at its actual UI size and in relevant
   themes/states.

Do not use real customer photos, credentials, access tokens, or private
material as sample avatars.
